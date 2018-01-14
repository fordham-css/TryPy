from django.http import HttpResponse
from django.template import loader

from .models import Question

"""
View Definitions
- Django uses callables (functions or classes) to deliver responses to requests
made to the server.
Each view is mapped to a url pattern in the application's urls.py module.
Django will deterime which view to call based on the url pattern captured.

Each view must accept `request` as its first parameter. This is an instance of
Django's HttpRequest object. It represents a request made to that view's url.
Views can also accept additional arguments, either positional or keyword. The
parameters passed to a view are handled by the url dispatcher.

Additionally, each view must return an instance of Django's HttpResponse
object. This is the response from the server to the client, and can include a
template with context data, a JSON file, or whatever you decide.

Views contain the logic that is executed when someone requests the page tied to
the callable. This where you get your webserver to do some processing for you.
"""


def index(request):
    """
    Return the last five Questions in the database
    Will render the index.html template with context data retrieved from the
    database.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))
