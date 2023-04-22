from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list_actives', views.list_actives, name="list_actives"),
    path('add_actives', views.add_actives, name="add_actives"),
    path('update_actives/<int:idactive>', views.update_actives, name="update_actives"),
    path('delete_actives/<int:idactive>', views.delete_actives, name="delete_actives"),
    
    path('list_user', views.list_user ,name='list_user'),
    path('add_user', views.add_user, name="add_user"),
    path('update_user/<int:iduser>', views.update_user, name="update_user"),
    path('delete_user/<int:iduser>', views.delete_user, name="delete_user"), 
]

