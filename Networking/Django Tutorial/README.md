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

**1. Creating the Project & Application**

#### Creating the project
The first thing you'll do when creating you own Django project is to have the django-admin command build your project directory for you. The command to start a new Django project is `django-admin startproject <project_name>`. In this example, the project has already been created. In our example the project is named TryPyDjango.

#### Django project directory
Inside of this directory, there will be one file and one directory: a `manage.py` file used for interacting with various Django tools, and a `<project_name>/` directory that contains project specific files. Namely, it contains a `settings.py` file for storing configuration variables, a `wsgi.py` file for serving your project through a WSGI-enabled web frameworked, and a `url.py` file for mapping requests to views. You can read the documentation for further explanation as to what each file does.

#### Creating the application
To build functional components in your Django project, you'll create applications in your project directory. The command to start an application is `python manage.py startapp <app_name>`. Again, the example app has already been created in the project directory, named `polls/`. The command will create a directory in your project directory with the name you gave it, and create some files in it. We'll touch on what each file does in the relevant tutorial for it.

**2. Creating the Database**

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
After writing the Python class representing the database table, you will need to run the SQL that generates the tables. Fortunately, Django has utilities to handle this for you. The process to create the database tables takes two steps, creating migrations and then running the migrations.

Migrations are Python files that contain commands that perform create, update, and delete operations on database tables. When you create a new model or make changes to an existing model, run the command `python manage.py makemigrations <app_name>`. This will create a Python file in the `<app_name>/migrations/` directory containing the generated Python code to perform your database operations. It is strongly advised that you rename the generated migration file, as the default name given by Django does not really describe what the migration accomplishes.

Once the migration has been created, the final step is to run the migration. Running the command `python manage.py migrate <app_name>` will run all unapplied migrations in the specified applications `migrations/` directory. The command will inform you of the operations it performs, such as creating or dropping tables & adding, deleting, and updating table columns.

#### Using the Django shell
Django offers an Object-Relation Mapper, or ORM, to provide an API for accessing the database for a project. You can import the model classes to query the database for records, alter attributes of an instance to update data, and save the instance to write changes back to the database. Besides interacting with the model classes in other Django modules, you can use the built-in shell to access the ORM. See an example below of using the shell with the models defined in `polls/models.py`:

```
46 // TryPyDjango //$ ./manage.py shell
Python 2.7.6 (default, Nov 23 2017, 15:49:48) 
Type "copyright", "credits" or "license" for more information.

# Import the models from the application
In [1]: from polls.models import Question, Choice

In [2]: # Use the objects attribute of a Django model to perform database operations through the API

In [3]: Question.objects.count()  # Returns number of objects in the table
Out[3]: 0

In [4]: # Can create an instance of Question to represent a record in the table

In [5]: # Pass attributes as keyword arguments to constructor

In [6]: question = Question(question_text='Is Everything Okay In Your World?')

In [7]: # Note that simply creating an instance of a Model does nothing to the database

In [8]: Question.objects.count()
Out[8]: 0

In [9]: # To actually save the record in the table, we need to call the save() method on the instance

In [10]: question.save()

In [11]: Question.objects.count()
Out[11]: 1

In [12]: # Once an instance of a Model is saved to the database, it has a primary key assosciated with it

In [13]: # This is either the attribute specified to be the primary key in the Model definition, or the default pk field generated by Django

In [14]: question.pk
Out[14]: 1

In [15]: # You can access record attributes using normal Python class attribute syntax

In [16]: question.question_text
Out[16]: 'Is Everything Okay In Your World?'

In [17]: question.pub_date
Out[17]: datetime.datetime(2018, 1, 14, 1, 43, 47, 920489, tzinfo=<UTC>)

In [18]: # Using the create() method of a Models object manager is a shortcut to instantiate and save an instance in one line

In [19]: question2 = Question.objects.create(question_text="Isn't She Lovely?")

In [20]: Question.objects.count()
Out[20]: 2

In [21]: question2.pk
Out[21]: 2

In [22]: question2.question_text
Out[22]: "Isn't She Lovely?"

In [23]: question2.pub_date
Out[23]: datetime.datetime(2018, 1, 14, 1, 49, 55, 828314, tzinfo=<UTC>)

In [24]: # Using the ORM to query the database

In [25]: # Django Model managers have a couple methods to help you access records in your database

In [26]: # To get a Model by attribute, use the get() method

In [27]: q = Question.objects.get(pk=1)

In [28]: q.question_text
Out[28]: u'Is Everything Okay In Your World?'

In [29]: # Can pass any attribute name to query

In [30]: q = Question.objects.get(question_text='Is Everything Okay In Your World?')

In [31]: q.pk
Out[31]: 1

In [33]: # Will raise a DoesNotExist exception if no object matching the query is found

In [34]: q = Question.objects.get(question_text='bogus question')
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
...
DoesNotExist: Question matching query does not exist.

In [35]: # Will raise a MultipleObjectsReturned if more than one object matching query is returned

In [36]: # If you want to retrieve multiple records, use the filter() method

In [37]: # For example, to find all the Questions published since yesterday

In [38]: from datetime import date, timedelta

In [39]: yesterday = date.today() - timedelta(days=1)

# The __gte appended to the field name evaluates to a >= operation in SQL.
# Django has a number of such options to query an attribute, like __isnull for
# checking  if a value is none and __in to check if value is in a specified iterable.
# Consult the docs for more information on these Field lookup options
In [40]: questions = Question.objects.filter(pub_date__gte=yesterday)

In [42]: # filter() doesn't return an instance of the Model, but rather a QuerySet object

In [43]: type(questions)
Out[43]: django.db.models.query.QuerySet

In [44]: # It functions similiar to the model manager for the class, you can perform additional queries, filters, and other operations on it

In [45]: questions.count()
Out[45]: 2

In [46]: # To access the records contained in a QuerySet, you can index them like Python lists

In [47]: question = questions[0]

In [48]: question.question_text
Out[48]: u'Is Everything Okay In Your World?'

In [49]: # You can use the first() and last() methods on a QuerySet to retrieve the respective record in the queryset

In [50]: question = questions.last()

In [51]: question.question_text
Out[51]: u"Isn't She Lovely?"

In [52]: # Constructing Foreign Key Relationships

In [53]: # You need to specify an instance of the Model to link to when creating a record of a Model with a foreign key attribute

In [54]: # For example, let's create a Choice record for our Question

In [55]: choice = Choice.objects.create(choice_text='Of course she is!', question=question)

In [56]: choice.pk
Out[56]: 1

# Can access the linked model by going through the foreign key on the instance
In [57]: choice.question
Out[57]: <Question: Isn't She Lovely?>

In [58]: choice.question.question_text
Out[58]: u"Isn't She Lovely?"

In [59]: choice.question.pub_date
Out[59]: datetime.datetime(2018, 1, 14, 1, 52, 18, 371467, tzinfo=<UTC>)

In [60]: # Note that deleting the Question record that our Choice record points to will delete our Choice as well

In [61]: question.question_text
Out[61]: u"Isn't She Lovely?"

In [62]: question.delete()
Out[62]: (2, {u'polls.Choice': 1, u'polls.Question': 1})

In [63]: Choice.objects.count()
Out[63]: 0
```

**3. Writing Views**

**4. Forms & Generic Views**

**5. Writing Unit Tests**

**6. Static File Serving**

**7. Working with the Admin Site**
