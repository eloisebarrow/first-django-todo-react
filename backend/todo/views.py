from django.shortcuts import render
from rest_frameworks import viewsets # viewsets base class provides the implementation for CRUD operations
from .serializers import TodoSerializer
from .models import Todo 

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()