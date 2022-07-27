from django.db import models

# Create your models here.


class Dishes(models.Model):
    dishname = models.CharField(max_length=120,unique=True)
    price = models.PositiveIntegerField(default=100)
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.dishname