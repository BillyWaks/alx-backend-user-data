#!/usr/bin/env python3
"""
Flask application that uses Auth for user authentication.
"""

from flask import Flask, jsonify
from auth import Auth

app = Flask(__name__)
auth = Auth()

@app.route('/create_user', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    This interacts only with Auth and not directly with the DB.
    """
    email = "user@example.com"  # Extract from request
    password = "password123"  # Extract from request
    user = auth.create_user(email, password)
    return jsonify({'email': user.email})

if __name__ == "__main__":
    app.run(debug=True)
