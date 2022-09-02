from re import T
from django.urls import path
from . import views

app_name='edit'
urlpatterns=[
    path('index/',views.index, name='index')
]