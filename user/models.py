from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user_image=models.FileField()
    name=models.CharField(max_length=50, verbose_name='İsim')
    surname=models.CharField(max_length=50, verbose_name='Soyisim')
    email=models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.name +' '+ self.surname #show how we want it to be displayed

