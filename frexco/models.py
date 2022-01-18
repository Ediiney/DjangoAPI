from tkinter import CASCADE
from django.db import models

# Create your models here.

class FrexcoDB(models.Model):
    name = models.CharField(max_length=30)
    fruta = models.CharField(max_length=30)
