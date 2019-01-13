from django.urls import path
from . import views

urlpatterns = [
    path(r'random/', views.RandomNumber.as_view()),
    path(r'random/plot/', views.index, name='index'),
]