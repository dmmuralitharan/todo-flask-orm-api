from flask import Blueprint
from src.controllers.todo_controller import get_todo_controller, get_todos_controller, add_todo_controller, update_todo_controller, delete_todo_controller

todo_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todo_bp.route('/', methods=['GET'])
def get_todos():
    return get_todos_controller()

@todo_bp.route('/', methods=['POST'])
def add_todo():
    return add_todo_controller()

@todo_bp.route('/<int:id>', methods=['GET'])
def get_todo(id):
    return get_todo_controller(id)

@todo_bp.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    return update_todo_controller(id)

@todo_bp.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return delete_todo_controller(id)