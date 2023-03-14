from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoItem

# Create your views here.
class TodoListView(ListView):
    model = TodoItem

class TodoDetailView(DetailView):
    model = TodoItem

class TodoCreateView(CreateView):
    model = TodoItem
    fields = ["title", "description"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = TodoItem
    fields = ["title", "description"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = TodoItem
    success_url = reverse_lazy("todo_list")

