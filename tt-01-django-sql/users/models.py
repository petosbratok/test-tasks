from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Subdivision(models.Model):
    title = models.CharField(max_length=100, default='', null=True)


    def __str__(self):
        return f'{self.title}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='', null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, null=True)
    tablemaster = models.BooleanField(default=False)


    def __str__(self):
        return f'Профиль пользователя {self.full_name}'
