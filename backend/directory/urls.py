from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from directory import views

router = routers.DefaultRouter()
router.register(r'directories', views.directoryView, 'directory')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('directoryAPI/', include(router.urls)),
]