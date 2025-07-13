# NomNom Food Bot 🍽️🌟

Welcome to NomNom Food Bot! This project is a delightful web-based food ordering system that lets you explore a multi-cuisine menu, place orders, and track them with ease. Built with a Flask backend, MySQL database, and a user-friendly interface, it's a fun way to experience technology while enjoying your favorite meals! You can also build it with Dialogflow for a conversational AI experience. 🍕🙌

## Why NomNom Matters? 🍴🌍

NomNom brings a variety of cuisines under one roof, from Butter Chicken to Sushi, making food ordering accessible and enjoyable. It's a step toward enhancing convenience and supporting food lovers everywhere! 

## What's This Project About? ✨

NomNom Food Bot is a beginner-friendly web app that allows you to:

📋 Browse a diverse menu with items like Spaghetti Carbonara, Tacos, and Falafel 

🛒 Add items to your cart and place orders with a simple form 

📦 Track your order status in real-time with a unique order ID 

✨🎇 Experience real-time cart updates with Flask or chat with the Dialogflow bot!

## What's in the Box? 📦

### Core Files:
🗃️`pandeyji_eatery.sql`: SQL script to set up the MySQL database

💻 `script.js`: JavaScript for cart and order form functionality 

🐍 `db_helper.py`: Python module for MySQL database interaction 

🔧 `generic_helper.py`: Utility functions for text processing 

🌐 `index.html`: Main webpage with menu and order sections 

🎨 `index.css`: Styling for the web interface 

🚀 `main.py`: Flask API for order processing 

📜 `requirements.txt`: Project dependencies 

### Dialogflow Option:
🤖 All JSON intent and entities files for creating an AI chatbot with ordering/tracking capabilities 

## Prerequisites 🛠️

🐍 Python 3.8+ 

📊 MySQL Server 

📚 Required libraries: `fastapi`, `mysql-connector-python`, `uvicorn` 

🌐 (Optional) Dialogflow Account for chatbot alternative 

🌐 Web Browser 

🍔😄 A Hungry Mind! 

  
## 🛠️ Tech Stack  

| Component       | Technology               |
|----------------|--------------------------|
| Frontend       | HTML5, CSS3, JavaScript  |
| Backend        | Python (FastAPI)         |
| NLP Engine     | Dialogflow               |
| Database       | MySQL                    |
| Deployment     | Localhost/Dialogflow ES  |

## How to Run This Project? 🚀

### For Flask Web App

#### Clone the Repository

bash

git clone [https://github.com/Archana-P-Nair/NomNom-Chatbot/.git
]
cd NomNom-Chatbot

#### Set Up the Environment

bash

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

#### Install dependencies:

bash

pip install -r requirements.txt

#### Set Up the Database

bash

mysql -u root -p < pandeyji_eatery.sql

Update DB_PASSWORD in db_helper.py with your MySQL password. 🔑

#### Run the Web App

bash

python main.py

Inside main.py

run uvicorn main:app --reload

Open your browser and go to http://127.0.0.1:8000 to use the app! 🌐

### For Dialogflow Chatbot

Create a Dialogflow agent at console.dialogflow.com.

Define intents for "Order Food," "Track Order," and "Menu Inquiry."

Connect to a webhook (e.g., Flask API) or use fulfillment for responses.

Embed the Dialogflow chatbot in index.html using the Dialogflow Web Demo's iframe code.

Test with voice/text inputs! 

## How Is It Useful? 🌟

🍱Convenient Ordering: Order food from multiple cuisines with ease. 

📡Real-Time Tracking: Stay updated on your order status. 

💻🤖Learning Tool: Great for learning web development, database integration, or conversational AI with Dialogflow! 

## Future Work 🌱

💳 Add Payment Integration: Include a payment gateway for online transactions. 

📱Mobile App: Port the project to a mobile platform for on-the-go ordering. 

👥More Features: Add user accounts, order history, and live chat support. 

🌮Expand Menu: Include more dishes and cuisines. 
