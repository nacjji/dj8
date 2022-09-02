from django.urls import path
from . import views

app_name='board'
urlpatterns=[
    path('index/',views.index,name='index'),
    path('detail/<bpk>',views.detail, name='detail'),
    path('update/<bpk>',views.update,name='update'),
    path('delete/<bpk>',views.delete,name='delete'),
    path('create/',views.create, name='create'),
    path('crepl/<bpk>',views.crepl,name='crepl'),
    path('cdelete/<bpk>/<rpk>',views.cdelete, name='cdelete'),
]
