from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import db_helper
import re
import random

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

inprogress_orders = {}


def get_str_from_food_dict(food_dict: dict):
    """Converts a dictionary of food items and quantities into a readable string."""
    if not food_dict:
        return ""
    return ", ".join([f"{qty} {item}" for item, qty in food_dict.items()])


@app.get("/")
async def read_root():
    return HTMLResponse("<html><body><h1>NomNom Chatbot Server is Running!</h1></body></html>")


@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    session_id = payload.get('session_id')
    message = payload['message']['text'].lower()

    if not session_id:
        return JSONResponse(status_code=400, content={"error": "Session ID is missing"})

    intent = "unknown"
    current_state = inprogress_orders.get(session_id, {}).get('state')

    # =========== RESTRUCTURED INTENT DETECTION BLOCK ===========
    # Prioritize state-dependent logic for more robust conversation flow.

    message_words = set(message.split())
    greeting_words = {'hi', 'hello', 'hey'}

    # 1. Handle state-dependent intents first
    if current_state == 'ordering':
        if any(word in message for word in ['no', 'nope', 'that\'s all', 'done', 'complete']):
            intent = 'complete_order'
        elif 'remove' in message or "don't want" in message:
            intent = 'remove_from_order'
        # If it looks like a food item (has a number), treat it as an add request.
        elif re.search(r'\d', message):
            intent = 'add_to_order'
        # Otherwise, the input is ambiguous in the ordering context.

    elif current_state == 'awaiting_order_id':
        if re.match(r'^\d+$', message):
            intent = 'track_order_provide_id'

    # 2. If no state-specific intent was found, check for general intents.
    if intent == "unknown":
        if greeting_words.intersection(message_words):
            intent = 'greeting'
        elif 'new order' in message or 'place an order' in message:
            intent = 'new_order'
        elif 'track' in message and 'order' in message:
            intent = 'track_order_start'
        # Allow starting an order with "add 1 pizza" even if not in 'ordering' state.
        elif 'add' in message and re.search(r'\d', message):
            intent = 'add_to_order'
    # =========== END OF RESTRUCTURED BLOCK ===========

    # Handle intents
    fulfillment_text = ""

    if intent == 'greeting':
        fulfillment_text = random.choice([
            "Hello! How can I help you? You can say 'New Order' or 'Track Order'!",
            "Good day! What can I do for you today?",
            "Greetings! How can I assist?"
        ])

    elif intent == 'new_order':
        inprogress_orders[session_id] = {'state': 'ordering', 'items': {}}
        fulfillment_text = "Let's get your order started! What would you like? (Example: '2 sushi' or '1 pizza and 2 tacos')"

    elif intent == 'add_to_order':
        # Ensure an order session exists
        if session_id not in inprogress_orders or inprogress_orders[session_id].get('state') != 'ordering':
            inprogress_orders[session_id] = {'state': 'ordering', 'items': {}}

        food_items_to_add = {}
        unmatched_parts = []

        parts = message.split(" and ")
        for part in parts:
            match = re.search(r'(\d+)\s+([a-zA-Z\s]+)|([a-zA-Z\s]+)\s+(\d+)', part.strip())
            if not match:
                unmatched_parts.append(part)
                continue

            quantity = int(match.group(1) or match.group(4))
            item_name = (match.group(2) or match.group(3)).strip().lower()

            matched_item = None
            for food_item_key in db_helper.food_prices.keys():
                if item_name in food_item_key.lower():
                    matched_item = food_item_key
                    break

            if matched_item:
                food_items_to_add[matched_item] = food_items_to_add.get(matched_item, 0) + quantity
            else:
                unmatched_parts.append(part)

        if food_items_to_add:
            current_order_items = inprogress_orders[session_id]['items']
            for item, qty in food_items_to_add.items():
                current_order_items[item] = current_order_items.get(item, 0) + qty

            order_str = get_str_from_food_dict(current_order_items)
            fulfillment_text = f"Added to your order. Current items: {order_str}. Anything else?"
            if unmatched_parts:
                fulfillment_text += f" I couldn't recognize these items: {', '.join(unmatched_parts)}."
        else:
            fulfillment_text = "I didn't quite catch that. Please specify items like '2 sushi' or '1 pizza'."

    elif intent == 'remove_from_order':
        if session_id in inprogress_orders and inprogress_orders[session_id]['items']:
            current_order = inprogress_orders[session_id]['items']
            items_to_remove_keys = [key for key in current_order if key.lower() in message]

            if items_to_remove_keys:
                removed_items_str = [key.capitalize() for key in items_to_remove_keys]
                for key in items_to_remove_keys:
                    del current_order[key]

                order_str = get_str_from_food_dict(current_order)
                fulfillment_text = f"Removed {', '.join(removed_items_str)}. "
                fulfillment_text += f"Your current order is: {order_str}." if order_str else "Your order is now empty."
            else:
                fulfillment_text = "That item isn't in your current order."
        else:
            fulfillment_text = "I don't have an active order for you to remove items from."

    elif intent == 'complete_order':
        if session_id in inprogress_orders and inprogress_orders[session_id]['items']:
            order = inprogress_orders[session_id]['items']
            order_id = db_helper.save_order_to_db(order)
            if order_id == -1:
                fulfillment_text = "Sorry, I couldn't process your order due to a backend error."
            else:
                total_price = db_helper.get_total_order_price(order_id)
                fulfillment_text = (f"Awesome. Your order is placed! Your order ID is #{order_id}. "
                                    f"The total is ${total_price:.2f}, payable on delivery.")
            del inprogress_orders[session_id]
        else:
            fulfillment_text = "I don't have an active order to complete. Please start a 'new order'."

    elif intent == 'track_order_start':
        inprogress_orders[session_id] = {'state': 'awaiting_order_id'}
        fulfillment_text = "Of course. Please provide your order ID."

    elif intent == 'track_order_provide_id':
        try:
            order_id = int(message)
            status = db_helper.get_order_status(order_id)
            fulfillment_text = f"The status for order #{order_id} is: {status}." if status else f"I couldn't find any order with the ID #{order_id}."
            if session_id in inprogress_orders:
                del inprogress_orders[session_id]
        except ValueError:
            fulfillment_text = "That doesn't look like a valid order ID. Please enter only the number."

    else: # intent == 'unknown'
        if current_state == 'ordering':
            fulfillment_text = "I didn't understand that. Please specify items like '2 sushi' or say 'done' to complete your order."
        else:
            fulfillment_text = "I'm sorry, I didn't understand that. You can say 'New Order' or 'Track Order'."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})