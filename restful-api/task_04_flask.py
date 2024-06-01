#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""


from flask import Flask
from flask import jsonify

"""Dictionary containing users, with a test user jane"""
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

"""Initialize the Flask application"""
app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


"""Route to get user names as JSON"""


@app.route("/data")
def data():
    """Get the list of user names"""
    usernames = list(users.keys())
    """Return the list of user names as JSON"""
    return jsonify(usernames)


"""Route to return the status OK"""


@app.route('/status')
def status():
    return 'OK'


"""Route to return details of a specific user"""


@app.route('/users/')
def get_user(username):
    return jsonify(users.get(username, "User not found"))


"""Route to add a new user via a POST request"""


@app.route('/add_user', methods=['POST'])
def add_user():
    """Get JSON data from the request"""
    new_user = request.get_json()
    username = new_user.get('username')
    """Add the new user to the users dictionary"""
    users[username] = new_user
    """Return a confirmation message with the added user's data"""
    return jsonify({"message": "User added", "user": new_user})


"""execut application Flask"""


if __name__ == "__main__":
    app.run()
