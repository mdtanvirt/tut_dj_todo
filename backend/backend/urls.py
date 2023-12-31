from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('directory/', include('directory.urls'))
]