from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, CreateView

from django.urls import reverse_lazy

from .models import Todo
# Create your views here.


#def todo_list(request):
    #todos = Todo.objects.all()

   #nomes = ["neymar, messi, cristiano ronaldo"]
    #return render(request, "todos/todo_list.html", {"todos": todos})



class TodoListView(ListView):

    model = Todo


class TodoCreateView(CreateView):

     model = Todo
     fields = ["title", "deadline"]
     success_url = reverse_lazy("todo_list")

