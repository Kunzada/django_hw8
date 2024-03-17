from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(requests):
    todos=todo.objects.all()
    return render(requests,"home.html",{'todos':todos})

def detail(requests,todo_id):
    todo_one=todo.objects.get(id=todo_id)
    return render(requests,"detail.html",{'todo':todo_one})

def create_todo(requests):
    if requests.method=="POST":
        title=requests.POST.get('title')
        image=requests.FILES.get('image')
        status=requests.POST.get('status')
        todo_create=todo.objects.create(title=title,image=image,status=status)
        return redirect('home')
    return render(requests,'create.html')

def update_todo(requests,edit_id):
    todos=todo.objects.get(id=edit_id)
    if requests.method=="POST":
        todos.title=requests.POST.get('title')
        todos.image=requests.FILES.get('image')
        todos.status=requests.POST.get('status')
        todos.save()
        return redirect('home')
    return render(requests,'edit.html',{'todo':todos})
def delete_todo(requests,todo_id):
    todo_one=todo.objects.get(id=todo_id)
    todo_one.delete()
    return redirect('home')

