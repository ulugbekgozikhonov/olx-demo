from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class User(Base, AbstractUser):
    photo = models.ImageField(upload_to="user/avatars/", null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    
