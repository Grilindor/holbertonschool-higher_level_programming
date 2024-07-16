#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    return render_template('items.html', items=data.get('items', []))


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source', 'json')  # Par défaut, source est 'json'

    if source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            products = cursor.fetchall()
            conn.close()

            # Convertir la liste de tuples en liste de dictionnaires
            products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]

            return render_template('product_display.html', products=products, error_message=None)

        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
            return render_template('product_display.html', products=None, error_message=error_message)

    else:
        error_message = "Wrong source: Please use 'json', 'csv', or 'sql' as source parameter."
        return render_template('product_display.html', products=None, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
