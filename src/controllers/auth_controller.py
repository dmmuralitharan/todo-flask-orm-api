from flask import request, jsonify
import bcrypt

from src import db
from src.models.user_model import User

def register_user_controller():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password required", "status": False}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists", "status": False}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        username=username,
        password=hashed_password.decode('utf-8'),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "status": True}), 201

def login_user_controller():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password required", "status": False}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({"message": "Invalid credentials", "status": False}), 401

    return jsonify({"message": "Login successful", "status": True}), 200
