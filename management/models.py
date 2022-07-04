from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Praticien(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)

class Patient(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)