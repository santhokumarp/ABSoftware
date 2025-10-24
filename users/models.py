from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class UserRole(models.TextChoices):
    ADMIN = 'admin','Admin'
    PROVIDER = 'provider', 'Provider'
    USER = 'user','User'

class User(models.Model):
    username = models.CharField(max_length=100, unique=True, )
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    date_joined = models.DateTimeField(default=timezone.now)

    USER_FIELD = 'username'
    REQUIRED_FIELDS =['email']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def __str__(self):
        return f"{self.username} ({self.role})"






    
    






