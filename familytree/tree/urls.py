from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('get_people/', views.get_people, name='get_people'),
   path('trash/', views.trash, name='trash')
]
