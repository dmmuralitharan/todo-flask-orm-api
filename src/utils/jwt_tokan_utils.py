from flask import current_app, request, jsonify
from datetime import datetime, timedelta
from functools import wraps
from src.models.user_model import User
import jwt

def generate_token(user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1), 
            'iat': datetime.utcnow(),  
            'user_id': user_id 
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm='HS256')
        return token
    except Exception as e:
        return str(e)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        print( current_app.config['SECRET_KEY'])

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
            print(token)

        if not token:
            return jsonify({'message': 'token is missing'}), 401

        try:
            tokan_data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=tokan_data['user_id']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 401

        return f(current_user, *args, **kwargs)
    return decorated
