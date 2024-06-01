#!/usr/bin/python3
"""Développer une API simple en utilisant Python avec Flask"""


from flask import Flask, jsonify, request
import socketserver
from http.server import SimpleHTTPRequestHandler


app = Flask(__name__)


# Dictionnaire des utilisateurs
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """Route de la page d'accueil"""
    return "Bienvenue dans l'API Flask !"


@app.route('/data')
def get_data():
    """Route pour obtenir tous les noms d'utilisateur"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Route de statut"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Route pour obtenir les informations d'un utili par nom d'utilisateur"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Route pour ajouter un nouvel utilisateur"""
    user_data = request.json
    username = user_data.get('username')
    if username and username not in users:
        users[username] = {
            "name": user_data.get('name'),
            "age": user_data.get('age'),
            "city": user_data.get('city')
        }
        return jsonify({"message": "Utilisa ajouté", "user": users[username]})
    else:
        return jsonify({"error": "Données invalides ou util existe déjà"}), 400


if __name__ == "__main__":
    import os
    from werkzeug.serving import run_simple

    PORT = int(os.environ.get('PORT', 8000))  # Vous pouvez définir le port ici

    # Démarrer le serveur Flask en utilisant werkzeug
    run_simple('0.0.0.0', PORT, app)


    # Utiliser socketserver pour servir les requêtes HTTP
    class FlaskRequestHandler(SimpleHTTPRequestHandler):
        """contais the class"""
        def do_GET(self):
            """contais the do_get"""
            if self.path.startswith('/'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Bienvenue dans l'API Flask via SimpleHTTPRequestHandler!")
            else:
                super().do_GET()

    with socketserver.TCPServer(("", PORT), FlaskRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
