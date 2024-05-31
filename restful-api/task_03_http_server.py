#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""


import http.server
import socketserver
import json


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


class SimpleHTTPRequestHandler(Handler):
    """creation of a subclass"""
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            response = json.dumps(status)
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            response = json.dumps(info)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")


"""it's run the server"""
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
