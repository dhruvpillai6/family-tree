from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.


def index(request):
    return HttpResponse('Hello')


def get_people(request):
    return render(request, 'tree/get_people.html', {'people': Person.nodes.all()})


def trash(request):
    return HttpResponse('Hiya')
