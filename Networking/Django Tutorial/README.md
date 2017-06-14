# Django TryPy Tutorial

### Directory Structure
```
Networking/
    Django Tutorial/ <- You are here
        README.md
        TryPyDjango/ <- site root directory
            manage.py
            TryPyDjango/ <- site specific settings
                settings.py
                urls.py
                wsgi.py
```

### Getting Setup

1. Ensure you have Django installed. If you installed the dependencies from the Networking requirements file you should already have it installed. If not, you should go do that! Read the README in the Networking directory to get that taken care of.

2. Next you will need to migrate the database to avoid getting a warning message. We'll cover this in a later section. To run the migrations, enter `python manage.py migrate` from the site root directory.

3. Finally, run `python manage.py runserver` and navigate to your localhost on any webbrowser (127.0.0.1:8000). You should see the homepage of the application we'll be using as our demo!
