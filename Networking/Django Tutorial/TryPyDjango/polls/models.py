import datetime

from django.db import models
from django.utils import timezone

"""
Model Definitions
- Django uses Python classes to define the shema for a project's database.
Each class represents one table in an SQL organization, with the attributes of
the class representing the columns for a record in the database.
Attributes are represented as various instances of ModelFields, defined in
Django's models module.
If an attribute is not explicitly defined as the primary key for a table,
Django will add one behind the scenes. This attribute can be reffered to by
either some_model.id or some_model.pk.
Since Django models are just Python classes, they can have defined methods that
operate on instances of the Model class.
You can import the model to perform queries in other modules in your
application by importing the models module. Example:
    `from .models import <ModelName>`.
"""


class Question(models.Model):
    # Adds a CHAR field to the Question table
    # Sets the max characters to 200
    question_text = models.CharField(max_length=200)

    # Adds a DATETIME field to the Question table
    # Gives it a human readable name, which is used in some DJango functions
    # Sets the field to the current date/time when saved for the first time
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    # NOTE: The auto_now_add field was added in this example and is absent in
    # Django tutorial. The author felt it relevant to show you how you can set
    # the default value of a DateTimeField attribute to the current time

    # Dunder str method
    # Defines behavior when instance of the class is typecasted to a string,
    # like when you print it.
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Adds a CHAR field to the Choice table
    # Set the max characters to 200
    choice_text = models.CharField(max_length=200)

    # Adds an INT field to the Choice table
    # Sets value to 0 when first created
    votes = models.IntegerField(default=0)

    # Sets a foreign key relationship on the Question table
    # Each Choice record is linked to a Question record

    # When a Question is deleted, the Choice records linked to it will be
    # deleted. There are other options you can pass to on_delete to specify the
    # behavior of deleting related models. Consult the Django documentation on
    # writing models to see the various options.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
