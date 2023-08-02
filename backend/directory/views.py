from django.shortcuts import render

from rest_framework import viewsets
from .serializers import DirectorySerializer
from .models import Directory

class directoryView(viewsets.ModelViewSet):
    serializer_class = DirectorySerializer
    queryset = Directory.objects.all()