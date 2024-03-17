from django.urls import path ,re_path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    re_path(r'^create',create_todo,name='create'),
    re_path(r'^detail/(?P<todo_id>\d+)/$', detail, name='detail'),
    re_path(r'^delete/(?P<todo_id>\d+)/$',delete_todo,name='delete'),
     re_path(r'^edit/(?P<edit_id>\d+)/$',update_todo,name='edit')
]