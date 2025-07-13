import re

# A mapping for text numbers to integers
num_map = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5
}


def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(quantity)} {food_item.capitalize()}" for food_item, quantity in food_dict.items()])


def find_closest_food_item(item_str: str):
    from db_helper import food_prices
    for item in food_prices.keys():
        if item in item_str:
            return item
    return None


def convert_to_int(num_str: str):
    if num_str.isdigit():
        return int(num_str)
    return num_map.get(num_str.lower(), 1)