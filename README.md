# TODO API

### Description
A todo application created with Django . It uses a simple REST API that allows users to create, retrieve, update, and delete items from a todo list.

Prerequisets
Django==4.1.7
python3

## How to run
```
git clone
```

```
pip install -r requirements.txt
```

* Start the Django development server by running `python3 manage.py runserver` in your terminal.

* Open a new terminal window and run the following commands 

* To register user 
Replace myusername and mypassword with your username and password

```
python3 client.py --register-user --username myusername --password mypassword
```


* To create a new todo item:

```
python3 client.py --create-todo --username myusername --password mypassword
```

* To list of all todo items

```
python3 client.py --get-todos  --username myusername --password mypassword
```

* To retrieve a specific todo item by its ID;
Replace `id` with an id of  task

```
python3 client.py --get-todo-by-id id --username myusername --password mypassword
```

To update a todo item:

```
python3 client.py --update-todo id --username myusername --password mypassword
```

To to delete a todo item:

```
python3 client.py --delete-todo id --username myusername --password mypassword
```



