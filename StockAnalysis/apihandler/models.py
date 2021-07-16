from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254,unique=True)
    message=models.TextField(max_length=1000)
    def __str__(self):
        return name