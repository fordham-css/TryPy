# Django TryPy Tutorial

## Directory Structure
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

## Getting Started

1. Ensure you have Django installed. If you installed the dependencies from the Networking requirements file you should already have it installed. If not, you should go do that! Read the README in the Networking directory to get that taken care of.

2. Next you will need to migrate the database to avoid getting a warning message. We'll cover this in a later section. To run the migrations, enter `python manage.py migrate` from the site root directory.

3. Finally, run `python manage.py runserver` and navigate to your localhost on any webbrowser (127.0.0.1:8000/polls/). You should see the homepage of the application we'll be using as our demo!


## Tutorial
This guide will follow the tutorial in the Django docs. The tutorial can be found [here](https://docs.djangoproject.com/en/1.9/intro/). For those entirely new to working with a web framework, it would be helpful to read over the Django at a glance guide. The final code is included in the project along with some helper comments. A brief outline of each topic can be found below.

**1. Creating the Project & Application**
------

#### Creating the project
The first thing you'll do when creating you own Django project is to have the django-admin command build your project directory for you. The command to start a new Django project is `django-admin startproject <project_name>`. In this example, the project has already been created. In our example the project is named TryPyDjango.

#### Django project directory
Inside of this directory, there will be one file and one directory: a `manage.py` file used for interacting with various Django tools, and a `<project_name>/` directory that contains project specific files. Namely, it contains a `settings.py` file for storing configuration variables, a `wsgi.py` file for serving your project through a WSGI-enabled web frameworked, and a `url.py` file for mapping requests to views. You can read the documentation for further explanation as to what each file does.

#### Creating the application
To build functional components in your Django project, you'll create applications in your project directory. The command to start an application is `python manage.py startapp <app_name>`. Again, the example app has already been created in the project directory, named `polls/`. The command will create a directory in your project directory with the name you gave it, and create some files in it. We'll touch on what each file does in the relevant tutorial for it.

**2. Creating the Database**
------

#### Configuring database settings
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

#### Writing the models
Django knows about an applications database schema by reading the application's `models.py` file. This file contains Python classes that map to database tables, with the class attributes corresponding to column names in the database table. See the `polls/models.py` file for notes on writing Django models.

#### Creating & Running migrations
After writing the Python class representing the database table, you will need to run the SQL that generates the tables. Fortunately, Django has utilities to handle this for you. The process to create the database tables takes two steps, creating migrations and then running the migrations. In order for your application to be available to the Django function, you need to register your app. To do so, add it to the INSTALLED_APPS list in the `settings.py` file.

```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
]
```

Migrations are Python files that contain commands that perform create, update, and delete operations on database tables. When you create a new model or make changes to an existing model, run the command `python manage.py makemigrations <app_name>`. This will create a Python file in the `<app_name>/migrations/` directory containing the generated Python code to perform your database operations. It is strongly advised that you rename the generated migration file, as the default name given by Django does not really describe what the migration accomplishes.

Once the migration has been created, the final step is to run the migration. Running the command `python manage.py migrate <app_name>` will run all unapplied migrations in the specified applications `migrations/` directory. The command will inform you of the operations it performs, such as creating or dropping tables & adding, deleting, and updating table columns.

#### Using the Django shell
Django offers an Object-Relation Mapper, or ORM, to provide an API for accessing the database for a project. You can import the model classes to query the database for records, alter attributes of an instance to update data, and save the instance to write changes back to the database. Besides interacting with the model classes in other Django modules, you can use the built-in shell to access the ORM. See an example below of using the shell with the models defined in `polls/models.py`:

```python
> ./manage.py shell
Python 2.7.6 (default, Nov 23 2017, 15:49:48)
Type "copyright", "credits" or "license" for more information.

# Import the models from the application
In [1]: from polls.models import Question, Choice

# Use the objects attribute of a Django model to perform database operations
# through the API

In [2]: Question.objects.count()  # Returns number of objects in the table
Out[2]: 0

# Can create an instance of Question to represent a record in the table
# Pass attributes as keyword arguments to constructor

In [3]: question = Question(question_text='Is Everything Okay In Your World?')

# Note that simply creating an instance of a Model does nothing to the database

In [4]: Question.objects.count()
Out[4]: 0

# To actually save the record in the table, we need to call the save() method on the
# instance

In [5]: question.save()

In [6]: Question.objects.count()
Out[6]: 1

# Once an instance of a Model is saved to the database, it has a primary key
# assosciated with it
# This is either the attribute specified to be the primary key in the Modeldefinition,
# or thedefault pk field generated by Django

In [7]: question.pk
Out[7]: 1

# You can access record attributes using normal Python class attribute syntax

In [8]: question.question_text
Out[8]: 'Is Everything Okay In Your World?'

In [9]: question.pub_date
Out[9]: datetime.datetime(2018, 1, 14, 1, 43, 47, 920489, tzinfo=<UTC>)

# Using the create() method of a Models object manager is a shortcut to instantiate
# and save an instance in one line

In [10]: question2 = Question.objects.create(question_text="Isn't She Lovely?")

In [11]: Question.objects.count()
Out[11]: 2

In [12]: question2.pk
Out[12]: 2

In [13]: question2.question_text
Out[13]: "Isn't She Lovely?"

In [14]: question2.pub_date
Out[14]: datetime.datetime(2018, 1, 14, 1, 49, 55, 828314, tzinfo=<UTC>)

# Using the ORM to query the database
# Django Model managers have a couple methods to help you access records
# in your database

# To get a Model by attribute, use the get() method

In [15]: q = Question.objects.get(pk=1)

In [16]: q.question_text
Out[16]: u'Is Everything Okay In Your World?'

# Can pass any attribute name to query

In [17]: q = Question.objects.get(question_text='Is Everything Okay In Your World?')

In [18]: q.pk
Out[18]: 1

# Will raise a DoesNotExist exception if no object matching the query is found

In [19]: q = Question.objects.get(question_text='bogus question')
Exception:
DoesNotExist                              Traceback (most recent call last)
...
DoesNotExist: Question matching query does not exist.

# Will raise a MultipleObjectsReturned if more than one object matching query
# is returned
# If you want to retrieve multiple records, use the filter() method

# For example, to find all the Questions published since yesterday

In [20]: from datetime import date, timedelta

In [21]: yesterday = date.today() - timedelta(days=1)

# The __gte appended to the field name evaluates to a >= operation in SQL.
# Django has a number of such options to query an attribute, like __isnull for
# checking  if a value is none and __in to check if value is in a specified iterable.
# Consult the docs for more information on these Field lookup options
In [22]: questions = Question.objects.filter(pub_date__gte=yesterday)

# filter() doesn't return an instance of the Model, but rather a QuerySet object

In [23]: type(questions)
Out[23]: django.db.models.query.QuerySet

# It functions similiar to the model manager for the class, you can perform
# additional queries, filters, and other operations on it

In [24]: questions.count()
Out[24]: 2

# To access the records contained in a QuerySet, you can index them like Python lists

In [25]: question = questions[0]

In [26]: question.question_text
Out[26]: u'Is Everything Okay In Your World?'

# You can use the first() and last() methods on a QuerySet to retrieve the
# respective record in the queryset

In [27]: question = questions.last()

In [28]: question.question_text
Out[28]: u"Isn't She Lovely?"

# Constructing Foreign Key Relationships
# You need to specify an instance of the Model to link to when creating a
# record of a Model with a foreign key attribute

# For example, let's create a Choice record for our Question

In [29]: choice = Choice.objects.create(choice_text='Of course she is!', question=question)

In [30]: choice.pk
Out[30]: 1

# Can access the linked model by going through the foreign key on the instance
In [31]: choice.question
Out[31]: <Question: Isn't She Lovely?>

In [32]: choice.question.question_text
Out[32]: u"Isn't She Lovely?"

In [33]: choice.question.pub_date
Out[33]: datetime.datetime(2018, 1, 14, 1, 52, 18, 371467, tzinfo=<UTC>)

# Note that deleting the Question record that our Choice record points to will
# delete our Choice as well

In [34]: question.question_text
Out[34]: u"Isn't She Lovely?"

In [35]: question.delete()
Out[35]: (2, {u'polls.Choice': 1, u'polls.Question': 1})

In [36]: Choice.objects.count()
Out[36]: 0
```

The topic in the Django tutorial covers the admin site shipped with Django. This is an application pre-built in Django projects that allows you to create, update, and delete database records through a UI. You can find more information about the admin site in the docs page. 

**3. Writing Views & Templates**
------

#### What is a view?

#### URL dispatchers

#### Rendering templates

**4. Forms & Generic Views**
------

**5. Writing Unit Tests**
------

**6. Static File Serving**
------
