import mysql.connector
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "<Enter your MySQL database password>"
DB_NAME = "pandeyji_eatery"


food_prices = {
    "butter chicken": 6.00,
    "spaghetti carbonara": 7.00,
    "pizza": 8.00,
    "tacos": 5.00,
    "sushi": 6.00,
    "pad thai": 9.00,
    "french onion soup": 4.00,
    "goulash": 7.00,
    "falafel": 5.00
}


def get_db_connection():
    """Establishes a connection to your MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        logging.info("Database connection successful.")
        return conn
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to database: {err}")
        return None


def get_next_order_id():
    """Fetches the next available order ID from your orders table."""
    conn = get_db_connection()
    if conn is None:
        return -1

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT MAX(order_id) FROM orders")
        max_id = cursor.fetchone()[0]
        next_id = (max_id or 0) + 1
        logging.info(f"Next order ID will be: {next_id}")
        return next_id
    except mysql.connector.Error as err:
        logging.error(f"Error getting next order ID: {err}")
        return -1
    finally:
        cursor.close()
        conn.close()


def save_order_to_db(order: dict):
    """Saves a new order and its items to your database tables."""
    conn = get_db_connection()
    if conn is None:
        return -1

    cursor = conn.cursor()
    try:
        next_order_id = get_next_order_id()
        if next_order_id == -1:
            return -1

       
        for food_item, quantity in order.items():
          
            cursor.execute("SELECT item_id FROM food_items WHERE LOWER(name) = %s", (food_item.lower(),))
            result = cursor.fetchone()
            if not result:
                logging.warning(f"Food item not found: {food_item}")
                continue

            item_id = result[0]

            
            cursor.execute("SELECT price FROM food_items WHERE item_id = %s", (item_id,))
            price = cursor.fetchone()[0]

           
            cursor.execute(
                "INSERT INTO orders (order_id, item_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
                (next_order_id, item_id, quantity, price * quantity)
            )

        
        cursor.execute(
            "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)",
            (next_order_id, "in progress")
        )

        conn.commit()
        logging.info(f"Order {next_order_id} saved to database.")
        return next_order_id

    except mysql.connector.Error as err:
        logging.error(f"Database error in save_order_to_db: {err}")
        conn.rollback()
        return -1
    finally:
        cursor.close()
        conn.close()


def get_order_status(order_id: int):
    """Retrieves the status of a given order ID from order_tracking table."""
    conn = get_db_connection()
    if conn is None:
        return None

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT status FROM order_tracking WHERE order_id = %s", (order_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        logging.error(f"Database error in get_order_status: {err}")
        return None
    finally:
        cursor.close()
        conn.close()


def get_total_order_price(order_id: int):
    """Calculates the total price for a given order ID."""
    conn = get_db_connection()
    if conn is None:
        return -1

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT SUM(total_price) FROM orders WHERE order_id = %s", (order_id,))
        total = cursor.fetchone()[0]
        return total if total else 0
    except mysql.connector.Error as err:
        logging.error(f"Database error in get_total_order_price: {err}")
        return -1
    finally:
        cursor.close()
        conn.close()
