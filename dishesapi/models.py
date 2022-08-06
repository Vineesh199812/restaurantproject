from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
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
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    date=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=('customer','dish')


    def __str__(self):
        return self.review

class Carts(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dishes,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)