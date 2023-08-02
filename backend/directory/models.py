from django.db import models

class Directory(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    businessName = models.CharField(max_length=120)
    address = models.TextField()
    businessStarted = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.email