from django.urls import path
from todolist.views import show_todolist
from todolist.views import register 
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import tambahin
from todolist.views import checklist
from todolist.views import hapus
from todolist.views import show_json
from todolist.views import add_todo

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', tambahin, name='create-task'),
    path('checklist/<int:pk>/', checklist, name='checklist'),
    path('hapus/<int:pk>/', hapus, name='hapus'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todo, name='add_todo')
]