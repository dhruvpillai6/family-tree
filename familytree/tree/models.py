from django.db import models
from django.forms import ModelForm
from neomodel import StringProperty, DateProperty, StructuredNode, Relationship
from django_neomodel import DjangoNode

# Create your models here.


class Person(DjangoNode):
    name = StringProperty()
    dob = DateProperty()
    spouse = Relationship('Person', 'SPOUSE')

    class Meta:
        app_label = 'tree'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob']
