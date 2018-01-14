from django.conf.urls import url

import views

"""
URL Definitions
- This defines the url patterns for the polls app, to route incoming requests
to the appropriate view callable.
Each url pattern consists of a regular expression, view callable, and optional
(but strongly advised!) name.

The regex is used to map an incoming url pattern (say /polls/) to the proper
view callable passed in the second positional argument. For example, the
previous url pattern would map to the function index() in the views module.

You can capture arguments in the url pattern to pass to the callable. For
example, the url pattern /polls/5/results/ would call the results() function in
the views module, passing in 5 as a keyword argument named 'question_id'.

Defining a name in the url pattern allows you to reverse the url pattern to a
url string. This comes in handy when building urls for your site, as it allows
you to easily maintain url schemes in your project. To reverse a url name you
can use the `reverse` shortcut included with Django.
> from django.core.urlresolvers import reverse
> reverse('index')
>>> u'/polls/'
"""


urlpatterns = [
    url(r'^$', views.index, name='index'),
]