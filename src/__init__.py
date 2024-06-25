from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app)

    app.config.from_object('src.config.Config')
    db.init_app(app)
    
    migrate = Migrate(app, db)

    from src.routes.auth_route import auth_bp
    from src.routes.todo_route import todo_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    return app