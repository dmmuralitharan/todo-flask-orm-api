from flask import request, jsonify
from src.models.todo_model import Todo
from src import db

def get_todos_controller(user):
    todos = Todo.query.filter_by(user_id=user.id).all()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    } for todo in todos])

def add_todo_controller(user):
    user_id = user.id
    data = request.get_json()
    new_todo = Todo(title=data['title'], description=data.get('description'), user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created', "status": 1}), 201

def get_todo_controller(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    })

def update_todo_controller(id):
    data = request.get_json()
    todo = Todo.query.get_or_404(id)
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify({'message': 'Todo updated', "status": 1})

def delete_todo_controller(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted', "status": 1})