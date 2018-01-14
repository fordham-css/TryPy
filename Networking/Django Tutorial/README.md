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

1. Creating the Application

2. Creating the Database

3. Writing Views

4. Forms & Generic Views

5. Writing Unit Tests

6. Static File Serving

7. Working with the Admin Site
