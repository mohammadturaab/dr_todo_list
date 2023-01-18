from django.shortcuts import render
from rest_framework import viewsets
from .serliaizers import TodoSerializer
from .models import Todo


# Create your views here.
class TodoView(viewsets.ModelView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
