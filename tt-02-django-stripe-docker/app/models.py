from django.db import models

class Item(models.Model):
    name = models.CharField(default='', max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
