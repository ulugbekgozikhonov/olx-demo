from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore
import datetime # type: ignore

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class User(Base, AbstractUser):
    photo = models.ImageField(upload_to="user/avatars/", null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    USERNAME_FIELD = "username"  
    REQUIRED_FIELDS = ["email", "phone_number"]  

    def __str__(self):
        return self.username  

class VerificationCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return (datetime.datetime.now(datetime.timezone.utc) - self.created_at).seconds > 300 