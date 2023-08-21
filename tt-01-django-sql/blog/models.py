from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Table(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    data = models.TextField(default='')
    length = models.IntegerField(default=30)

    def __str__(self):
        return self.title
