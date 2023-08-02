from django.contrib import admin

from .models import Directory

class directoryAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phone', 'businessName', 'address', 'businessStarted')

# Register model to admin panel
admin.site.register(Directory, directoryAdmin)