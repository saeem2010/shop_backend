from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, default='')  # Provide a default value
    address = models.TextField(blank=True, default='')  # Provide a default value

    def __str__(self):
        return self.user.username
