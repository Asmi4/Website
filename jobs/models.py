from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length= 200)