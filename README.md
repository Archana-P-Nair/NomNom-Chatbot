NomNom Food Bot 🍽️🌟
Welcome to NomNom Food Bot! This project is a delightful web-based food ordering system that lets you explore a multi-cuisine menu, place orders, and track them with ease. Built with a Flask backend, MySQL database, and a user-friendly interface, it’s a fun way to experience technology while enjoying your favorite meals! You can also build it with Dialogflow for a conversational AI experience. 🍕🙌
Why NomNom Matters? 🚀❤️
NomNom brings a variety of cuisines under one roof, from Butter Chicken to Sushi, making food ordering accessible and enjoyable. It’s a step toward enhancing convenience and supporting food lovers everywhere! 🌍🍴
What's This Project About? ✨
NomNom Food Bot is a beginner-friendly web app that allows you to browse a menu, add items to your cart, place orders, and track their status. Powered by a MySQL database and a Flask API, it offers a seamless experience for ordering food online! Alternatively, use Dialogflow to create a voice/text-based chatbot for ordering. 🌐🍽️

Browse a diverse menu with items like Spaghetti Carbonara, Tacos, and Falafel. 📋
Add items to your cart and place orders with a simple form. 🛒
Track your order status in real-time with a unique order ID. 📦
Real-Time Magic: See your cart update instantly as you order with Flask, or chat with the Dialogflow bot! ✨🎇

What's in the Box? 📦

pandeyji_eatery.sql: SQL script to set up the MySQL database with food items and orders. 🗃️
script.js: JavaScript for cart and order form functionality. 💻
db_helper.py: Python module to interact with the MySQL database. 🐍
generic_helper.py: Utility functions for text processing. 🔧
index.html: The main webpage with menu, cart, and order sections (with optional Dialogflow chat integration). 🌐
index.css: Styling for the web interface. 🎨
main.py: Flask API to handle order processing and tracking. 🚀
requirements.txt: Dependencies required to run the project. 📜
Dialogflow Option: Use Dialogflow to create an AI chatbot with intents for ordering and tracking. 🤖

Some Prerequisites 🛠️

Python 3.8+: Make sure it's installed on your computer. 🐍
MySQL Server: Install and set up a MySQL server. 📊
Libraries: Install fastapi, mysql-connector-python, and uvicorn. 📚
Dialogflow Account: Sign up for Dialogflow to build the chatbot alternative. 🌐
Web Browser: For accessing the web app or testing the chatbot. 🌐
A Hungry Mind: Ready to explore food ordering tech! 🍔😄

How to Run This Project? 🚀
For Flask Web App:

Clone the Repository  
git clone https://github.com/your-username/nomnom-food-bot.git
cd nomnom-food-bot


Set Up the Environment  

Create a virtual environment:  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:  pip install -r requirements.txt




Set Up the Database  

Install MySQL and create a database using the pandeyji_eatery.sql script:  mysql -u root -p < pandeyji_eatery.sql


Update DB_PASSWORD in db_helper.py with your MySQL password. 🔑


Run the Web App  

Start the Flask server:  python main.py


Open your browser and go to http://127.0.0.1:8000 to use the app! 🌐


Test It  

Browse the menu, add items to your cart, fill out the order form, and track your order! 🍕📤



For Dialogflow Chatbot:

Set Up Dialogflow  

Create a Dialogflow agent at console.dialogflow.com.
Define intents for "Order Food," "Track Order," and "Menu Inquiry."
Connect to a webhook (e.g., Flask API) or use fulfillment for responses.


Integrate with Web  

Embed the Dialogflow chatbot in index.html using the Dialogflow Messenger.
Test with voice/text inputs! 🤖



How Is It Useful? 🌟

Convenient Ordering: Order food from multiple cuisines with ease. 🍱
Real-Time Tracking: Stay updated on your order status. 📡
Learning Tool: Great for learning web development, database integration, or conversational AI with Dialogflow! 💻🤖

Future Work 🌱

Add Payment Integration: Include a payment gateway for online transactions. 💳
Mobile App: Port the project to a mobile platform for on-the-go ordering. 📱
More Features: Add user accounts, order history, and live chat support. 👥
Expand Menu: Include more dishes and cuisines. 🌮

Happy Eating, and Have Fun with NomNom! 🍽️😊
Happy coding and experimenting! Feel free to contribute or suggest improvements. 🌟👩‍💻👨‍💻
Last updated: 02:06 PM IST on Sunday, July 13, 2025.
