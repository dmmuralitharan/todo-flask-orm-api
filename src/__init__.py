from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    # app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db)

    from src.routers.todo_route import bp
    app.register_blueprint(bp)

    return app