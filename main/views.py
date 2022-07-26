
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import CreateNewList


def index(request, id):
    todolists = ToDoList.objects.get(id = id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for task in todolists.task_set.all():
                if request.POST.get("c" + str(task.id)) == "clicked":
                    task.complete = True
                else:
                    task.complete = False
                task.save()
        elif request.POST.get("newTask"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                todolists.task_set.create(text=txt, complete=False)
            else:
                print("invalid")
    return render(request, "main/list.html", {'todolists':todolists})

def createList(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todoList = ToDoList(name=name)
            todoList.save()
            request.user.todolist.add(todoList)
        return HttpResponseRedirect("/%i" %todoList.id)
    else:
        form = CreateNewList()
    return render(request, "main/create.html", {"form" : form})

def home(request):
    return render(request, "main/home.html")

def view(request):
    #user = request.user
    return render(request, "main/view.html", {})