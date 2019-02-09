
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello,name="homepage"),
    path('about', views.about,name="about"),
    path('wordcount', views.wordcount,name="wordcount"),


]
