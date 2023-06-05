import os
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path= os.path.join(os.getcwd(), "projects", "static", "img")) # Janky surely, but works