from django.db import models

# Create your models here.

class Sample(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Email = models.EmailField()