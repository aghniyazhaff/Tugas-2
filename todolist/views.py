from django.shortcuts import render
from todolist.models import Todolist
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from ast import Delete
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    todolist_data = Todolist.objects.filter(user=request.user)
    context = { 
        "nama": username,
        "todo_list": todolist_data,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def checklist(request, pk):

    temp = Todolist.objects.get(id=pk)
    if (temp.status == False):
        temp.status = True
    else :
        temp.status = False
    temp.save()

    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def hapus(request, pk):
    item = Todolist.objects.filter(pk=pk)
    item.delete()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def tambahin(request):
    context = {}
    if request.method == "POST":
        temp = Todolist(user=request.user, title=request.POST.get('todo'), description=request.POST.get('description'))
        temp.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html",context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response