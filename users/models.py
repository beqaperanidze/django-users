from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    role_choices = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]
    role = models.CharField(max_length=20, choices=role_choices, default='user')

    def __str__(self):
        return self.username
