from flask import Blueprint
from src.controllers.todo_controller import get_todo_controller, get_todos_controller, add_todo_controller, update_todo_controller, delete_todo_controller

from src.utils.jwt_token_utils import token_required

todo_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todo_bp.route('/', methods=['GET'])
@token_required
def get_todos(current_user):
    return get_todos_controller(current_user)

@todo_bp.route('/', methods=['POST'])
@token_required
def add_todo(current_user):
    return add_todo_controller(current_user)

@todo_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_todo(current_user, id):
    return get_todo_controller(id)

@todo_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_todo(current_user, id):
    return update_todo_controller(id)

@todo_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, id):
    return delete_todo_controller(id)