# Django TryPy Tutorial

### Directory Structure
```
Networking/
    Django Tutorial/ <- You are here
        README.md
        TryPyDjango/ <- site root directory
            manage.py
            polls/ <- application we'll be working on
                migrations/
                __init__.py
                admin.py
                apps.py
                models.py
                tests.py
                urls.py
                views.py
            TryPyDjango/ <- site specific settings
                settings.py
                urls.py
                wsgi.py
```

### Getting Started

1. Ensure you have Django installed. If you installed the dependencies from the Networking requirements file you should already have it installed. If not, you should go do that! Read the README in the Networking directory to get that taken care of.

2. Next you will need to migrate the database to avoid getting a warning message. We'll cover this in a later section. To run the migrations, enter `python manage.py migrate` from the site root directory.

3. Finally, run `python manage.py runserver` and navigate to your localhost on any webbrowser (127.0.0.1:8000/polls/). You should see the homepage of the application we'll be using as our demo!


### Tutorial
This guide will follow the tutorial in the Django docs. The tutorial can be found [here](https://docs.djangoproject.com/en/1.9/intro/). For those entirely new to working with a web framework, it would be helpful to read over the Django at a glance guide. The final code is included in the project along with some helper comments. A brief outline of each topic can be found below.

1. Creating the Project & Application

##### Creating the project
The first thing you'll do when creating you own Django project is to have the django-admin command build your project directory for you. The command to start a new Django project is `django-admin startproject <project_name>`. In this example, the project has already been created. In our example the project is named TryPyDjango.

##### Django project directory
Inside of this directory, there will be one file and one directory: a `manage.py` file used for interacting with various Django tools, and a `<project_name>/` directory that contains project specific files. Namely, it contains a `settings.py` file for storing configuration variables, a `wsgi.py` file for serving your project through a WSGI-enabled web frameworked, and a `url.py` file for mapping requests to views. You can read the documentation for further explanation as to what each file does.

##### Creating the application
To build functional components in your Django project, you'll create applications in your project directory. The command to start an application is `python manage.py startapp <app_name>`. Again, the example app has already been created in the project directory, named `polls/`. The command will create a directory in your project directory with the name you gave it, and create some files in it. We'll touch on what each file does in the relevant tutorial for it.

2. Creating the Database

##### Configuring database settings
By default, Django uses SQLite3 as the database driver. This is suitable for testing and local development, but on production servers a more powerful database engine, like PostgreSQL or MySQL would be better suited for the task. You can find the database configuration in the settings.py file in the project config directory
```
# TryPy/Networking/Django Tutorial/TryPyDjango/TryPyDjango/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
ENGINE is the dotted path of the database engine to use in the project, and NAME is the filepath of the database file. For other database engines, additional options like the database host and password must be specified. Consult the docs to see examples of how to set database configurations.

##### Writing the models
Django knows about an applications database schema by reading the application's `models.py` file. This file contains Python classes that map to database tables, with the class attributes corresponding to column names in the database table. See the `polls/models.py` file for notes on writing Django models.

##### Creating & Running migrations
After writing the Python class representing the database table, you will need to run the SQL that generates the tables. Fortunately, Django has utilities to handle this for you. The process to create the database tables takes two steps, creating migrations and then running the migrations.

Migrations are Python files that contain commands that perform create, update, and delete operations on database tables. When you create a new model or make changes to an existing model, run the command `python manage.py makemigrations <app_name>`. This will create a Python file in the `<app_name>/migrations/` directory containing the generated Python code to perform your database operations. It is strongly advised that you rename the generated migration file, as the default name given by Django does not really describe what the migration accomplishes.

Once the migration has been created, the final step is to run the migration. Running the command `python manage.py migrate <app_name>` will run all unapplied migrations in the specified applications `migrations/` directory. The command will inform you of the operations it performs, such as creating or dropping tables & adding, deleting, and updating table columns.

##### Using the Django shell

3. Writing Views

4. Forms & Generic Views

5. Writing Unit Tests

6. Static File Serving

7. Working with the Admin Site
