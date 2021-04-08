from django.db import models

# Create your models
from admin_proj1 import settings


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=100)
    branch = models.CharField(max_length=200)


    def __str__(self):
        return self.name

