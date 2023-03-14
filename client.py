import requests
import argparse


API_BASE_URL = 'http://localhost:8000/todoapp/api/'


TODO_LIST_ENDPOINT = API_BASE_URL + 'todos/'
TODO_DETAIL_ENDPOINT = API_BASE_URL + 'todos/{}/'


def print_response_data(response):
    print('Status code:', response.status_code)
    print('Response data:', response.json())


def get_todos(username, password):
    response = requests.get(TODO_LIST_ENDPOINT, auth=(username, password))
    print_response_data(response)

def get_todo_by_id(todo_id, username, password):
    response = requests.get(TODO_DETAIL_ENDPOINT.format(todo_id), auth=(username, password))
    print_response_data(response)


def create_todo(username, password):
    new_todo = {
        'title': input("Enter todo title: "),
        'description': input("Enter todo description: ")
    }
    response = requests.post(TODO_LIST_ENDPOINT, data=new_todo, auth=(username, password))
    print_response_data(response)


def update_todo(todo_id, username, password):
    updated_todo = {
        'title': input("Enter new todo title: "),
        'description': input("Enter new todo description: ")
    }
    response = requests.put(TODO_DETAIL_ENDPOINT.format(todo_id), data=updated_todo, auth=(username, password))
    print_response_data(response)

def delete_todo(todo_id, username, password):
    response = requests.delete(TODO_DETAIL_ENDPOINT.format(todo_id), auth=(username, password))
    print_response_data(response)

def register_user(username, password):
    new_user = {
        'username': input("Enter a new username: "),
        'password': input("Enter a new password: ")
    }
    response = requests.post(API_BASE_URL + 'users/', data=new_user, auth=(username, password))
    print_response_data(response)


parser = argparse.ArgumentParser(description='Todo app CLI')
parser.add_argument('--username', required=True, help='Username for authentication')
parser.add_argument('--password', required=True, help='Password for authentication')
parser.add_argument('--get-todos', action='store_true', help='Get all todos')
parser.add_argument('--get-todo-by-id', type=int, help='Get a specific todo by ID')
parser.add_argument('--create-todo', action='store_true', help='Create a new todo')
parser.add_argument('--update-todo', type=int, help='Update a todo by ID')
parser.add_argument('--delete-todo', type=int, help='Delete a todo by ID')
parser.add_argument('--register-user', action='store_true', help='Register a new user')


args = parser.parse_args()

if args.get_todos:
    get_todos(args.username, args.password)
elif args.get_todo_by_id:
    get_todo_by_id(args.get_todo_by_id, args.username, args.password)
elif args.create_todo:
    create_todo(args.username, args.password)
elif args.update_todo:
    update_todo(args.update_todo, args.username, args.password)
elif args.delete_todo:
    delete_todo(args.delete_todo, args.username, args.password)
elif args.register_user:
    register_user(args.username, args.password)