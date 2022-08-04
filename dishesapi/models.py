from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Dishes(models.Model):
    dishname = models.CharField(max_length=120,unique=True)
    price = models.PositiveIntegerField(default=100)
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.dishname

class Reviews(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dishes,on_delete=models.CASCADE)
    review=models.CharField(max_length=120)
    rating=models.PositiveIntegerField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review

class Carts(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dishes,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)