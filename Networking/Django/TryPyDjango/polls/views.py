from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

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

The easiest way to return an HTML template populated with some data you've
retrieved in the view is to render a template. This shortcut function takes the
request passed to the view, a template to render, and an optional context
dictionary used to fill out variables in the template.

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
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    Return details of the Question passed in the url
    Django will pass this view a paramter named question_id, corresponding to
    the positional value in the url. The url dispatcher defines where in the
    url the question_id should be specified.
    """
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """Return the results of the Question passed in the url"""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """Procces a vote for the Question passed in the url"""
    return HttpResponse("You're voting on question %s." % question_id)
