from flask import request, make_response, jsonify
import bcrypt
import os
import jwt

from src import db
from src.models.user_model import User
from src.utils.jwt_token_utils import generate_token


def register_user_controller():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return (
            jsonify({"message": "Username and password required", "status": 0}),
            400,
        )

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists", "status": 2}), 400

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    new_user = User(
        username=username,
        password=hashed_password.decode("utf-8"),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "status": 1}), 201


def login_user_controller():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return (
            jsonify({"message": "Username and password required", "status": 0}),
            400,
        )

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.checkpw(
        password.encode("utf-8"), user.password.encode("utf-8")
    ):
        return jsonify({"message": "Invalid credentials", "status": 0}), 401

    token = generate_token(user.id)
    return jsonify({"message": "Login successful", "token": token, "status": 1}), 200


blacklisted_tokens = set()
def logout_user_controller():
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            blacklisted_tokens.add(token)
            return jsonify({"message": "Logged out successfully", "status": 1}), 200
        return jsonify({"message": "Logged out successfully", "status": 0}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired", "status": 0}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token", "status": 0}), 401
    except Exception as e:
        return jsonify({"error": str(e), "status": 0}), 401


def token_is_blacklisted(token):
    return token in blacklisted_tokens