# Learning Flask and SQLite by Building a Todo App

## Table Of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setting Up Your Environment](#setting-up-your-environment)
4. [Creating the Flask Application](#creating-the-flask-application)
5. [Creating the SQLite Database](#creating-the-sqlite-database)
7. [Creating Templates](#creating-the-templates)
8. [Testing the App](#testing-the-app)
9. [Conclusion](#conclusion)
10. [Resources](#resources)

### Introduction

Throughout this tutorial, we will learn the basics of the Python Flask framework and the database engine SQLite by building a simple todo app. I find that the easiest way to learn certain programming concepts/tools is through making stuff!

Check out the github repository for the todo app [here!](https://github.com/GAchuzia/yag-todo)

### Prequisites

I'm going to assume you are familiar and comfortable programming in Python, SQL, HTML and CSS. The main goal of this project is to learn new tools (Flask and SQLite) with pre-established programming fundamentals.

### Setting Up Your Environment

In a directory of your choosing, make a project folder called `todo-app`, and create a Python virtual environment within that project folder where you can type the command `pip install Flask`.

```bash
C:directory/of/your/choosing/todo-app
C:directory/of/your/choosing/todo-app python -m venv venv
C:directory/of/your/choosing/todo-app/venv/Scripts activate
(venv) C:directory/of/your/choosing/todo-app pip install Flask 
```

Our project will contain the libraries needed for the todo app within this venv, so don't deactivate it!  

### Creating the Flask Application

In the `todo-app` we're going to make an `app.py`, `index.html`, and `index.css` files. The index.html file should be placed ina folder called `templates`, and the `index.css` file in a folder called `static`. Flask uses these folders for static and dynamic content, respectively.  

```bash
todo-app/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── index.css
```

The `app.py` file defines the web application we want to build. We import modules from the Flask framework:  
`Flask`: Creates an instance of the web application.  
`render_template`: Renders HTML templates which allows us to dynamically generate HTML.  
`request`: An object that contians info about incoming requests (e.g. form data, query parameters).
`url_for`: Generates URLs based on endpoint names in our applciation.  
`redirect`: Redirects the user to a different endpoint or URL within the app.  

The `database` module contains functions used to interact with our SQLite databse (more about that [here](#creating-the-sqlite-database)).

#### Routes

The file has serval "routes" which represent different URL endpoints that use the `@app.route` decorator. We'll go over the home/index page route as an overview.

```python
from flask import Flask, render_template, request, url_for, redirect
from database import connect_to_db, get_db

app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def index():
    db = get_db()
    tasks_getter = db.execute("select * from todolist")
    all_db_tasks = tasks_getter.fetchall()
    return render_template("index.html", all_db_tasks = all_db_tasks)
```

### Creating the SQLite Database

### Testing the App


### Conclusion

### Resources

[Project Github repo: GAchuzia/yag-todo](https://github.com/GAchuzia/yag-todo)  
[Flask Docs: Qiuckstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
