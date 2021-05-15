from flask import Blueprint, render_template, redirect, url_for, request
from ..extensions import mongo
from bson.objectid import ObjectId


main = Blueprint('main', __name__)


@main.route('/')
def index():
    todo_collection = mongo.db.todos
    todos = todo_collection.find()
    return render_template('index.html', todos=todos)


@main.route('/add_todo', methods=['POST'])
def add_todo():
    todo_collection = mongo.db.todos
    if request.method == 'POST':
        value = request.form['new-todo']
        todo_collection.insert_one({'text': value, 'completed': False})
    return redirect(url_for('main.index'))


@main.route('/complete_todo/<uid>')
def complete_todo(uid):
    todo_collection = mongo.db.todos
    todo_item = todo_collection.find_one({"_id": ObjectId(uid)})
    todo_item['completed'] = not todo_item['completed']
    todo_collection.save(todo_item)
    return redirect(url_for('main.index'))


@main.route('/delete_completed')
def delete_completed():
    todo_collection = mongo.db.todos
    todo_collection.delete_many({'completed': True})
    return redirect(url_for('main.index'))


@main.route('/delete_all')
def delete_all():
    todo_collection = mongo.db.todos
    todo_collection.delete_many({})
    return redirect(url_for('main.index'))

@main.route('/mark_all_complete')
def mark_all_completed():
    todo_collection = mongo.db.todos
    todos = todo_collection.find()
    for todo in todos:
        todo['completed'] = True
        todo_collection.save(todo)
    return redirect(url_for('main.index'))
