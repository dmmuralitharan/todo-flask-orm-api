from flask import request,make_response, jsonify
import bcrypt

from src import db
from src.models.user_model import User
from src.utils.jwt_tokan_utils import generate_token

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
    
    token = generate_token(user.id)
    return jsonify({"message": "Login successful","tokan": token, "status": True}), 200

def logout_user_controller():
    pass