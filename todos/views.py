from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo
# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()

    nomes = ["neymar, messi, cristiano ronaldo"]
    return render(request, "todos/todo_list.html", {"todos": todos})
