import requests
import argparse


API_BASE_URL = 'http://localhost:8000/todoapp/api/'


TODO_LIST_ENDPOINT = API_BASE_URL + 'todos/'
TODO_DETAIL_ENDPOINT = API_BASE_URL + 'todos/{}/'


def print_response_data(response):
    print('Status code:', response.status_code)
    print('Response data:', response.json())


def get_todos():
    response = requests.get(TODO_LIST_ENDPOINT)
    print_response_data(response)


def get_todo_by_id(todo_id):
    response = requests.get(TODO_DETAIL_ENDPOINT.format(todo_id))
    print_response_data(response)


def create_todo():
    new_todo = {
        'title': input("Enter todo title: "),
        'description': input("Enter todo description: ")
    }
    response = requests.post(TODO_LIST_ENDPOINT, data=new_todo)
    print_response_data(response)


def update_todo(todo_id):
    updated_todo = {
        'title': input("Enter new todo title: "),
        'description': input("Enter new todo description: ")
    }
    response = requests.put(TODO_DETAIL_ENDPOINT.format(todo_id), data=updated_todo)
    print_response_data(response)


def delete_todo(todo_id):
    response = requests.delete(TODO_DETAIL_ENDPOINT.format(todo_id))
    print_response_data(response)


parser = argparse.ArgumentParser(description='Todo app CLI')
parser.add_argument('--get-todos', action='store_true', help='Get all todos')
parser.add_argument('--get-todo-by-id', type=int, help='Get a specific todo by ID')
parser.add_argument('--create-todo', action='store_true', help='Create a new todo')
parser.add_argument('--update-todo', type=int, help='Update a todo by ID')
parser.add_argument('--delete-todo', type=int, help='Delete a todo by ID')


args = parser.parse_args()

if args.get_todos:
    get_todos()
elif args.get_todo_by_id:
    get_todo_by_id(args.get_todo_by_id)
elif args.create_todo:
    create_todo()
elif args.update_todo:
    update_todo(args.update_todo)
elif args.delete_todo:
    delete_todo(args.delete_todo)
