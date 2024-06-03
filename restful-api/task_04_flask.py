#!/usr/bin/python3
# Import necessary modules from Flask
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Dictionary to store user data
users = {}

# Route to display a welcome message at the home endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to return a list of usernames as JSON data
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Route to return a simple "OK" message
@app.route("/status")
def status():
    return "OK"

# Route to retrieve details of a specific user based on username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user via a POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

# Run the Flask application if the script is executed directly
if __name__ == "__main__":
    app.run()
