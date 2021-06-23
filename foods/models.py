from django.db import models


class food(models.Model):
    name= models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='foods/')

    def __str__(self):
        return self.name

