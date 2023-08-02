from django.shortcuts import render
from rest_framework import viewsets
from .serializers import todoSerializer
from .models import Todo

class todoView(viewsets.ModelViewSet):
    serializer_class = todoSerializer
    queryset = Todo.objects.all()