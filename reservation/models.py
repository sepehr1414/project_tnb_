from django.db import models
from django.db.models.fields import CharField

class reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone= models.CharField(max_length=30)
    number= models.IntegerField()
    date= models.DateField(auto_now=False,auto_now_add=False)
    time=models.TimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name
