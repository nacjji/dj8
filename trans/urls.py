from django.urls import path
from . import views
app_name='trans'
urlpatterns=[
    path('index/',views.index, name='index'),
    # path('tvoice/',views.tvoice, name='tvoice')
]