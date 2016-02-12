#!flask/bin/python
from flask import Flask
from flask import abort
from flask import jsonify
from flask import make_response
from flask import request
from flask import url_for

import helper

app = Flask(__name__)

tasks = [
  {
    'id': 1,
    'title': u'Buy groceries',
    'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
    'done': False
  },
  {
    'id': 2,
    'title': u'Learn Python',
    'description': u'Need to find a good Python tutorial on the web', 
    'done': False
  }
]

@app.route('/')
def index():
  helper.foo()
  return "Hello, World!"

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
  return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  # task = [task for task in tasks if task['id'] == task_id]
  # Instead of filter, find:
  try:
    task = next(task for task in tasks if task['id'] == task_id)
  except StopIteration:
    abort(404)
  return jsonify({'task': task})

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
  if not request.json or not 'title' in request.json:
    abort(400)
  task = {
    'id': tasks[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
  }
  tasks.append(task)
  return jsonify({'task': task}), 201

def make_public_task(task):
  new_task = {}
  for field in task:
    if field == 'id':
      new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
    else:
      new_task[field] = task[field]
  return new_task

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
