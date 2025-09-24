from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

  phone_number = models.CharField(
    max_length=15,
    unique=True,
    blank=True,
    null=True
  )
  
  avatar = models.ImageField(
    upload_to='images/%y/%m/%d'
  )
  
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField( unique=True)

  def __str__(self):
    return self.username