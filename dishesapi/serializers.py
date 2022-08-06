

from rest_framework import serializers
from dishesapi.models import Dishes,Reviews
from django.contrib.auth.models import User

class DishesSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    dishname=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()

    def validate(self,data):
        cost=data.get("price")
        if cost<0:
            raise serializers.ValidationError("invalid price")
        return data

class DishesModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Dishes
        fields="__all__"

    def validate(self, data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=["review","rating"]

    def create(self, validated_data):
        user=self.context.get("user")
        dish=self.context.get("dish")
        return Reviews.objects.create(customer=user,dish=dish,**validated_data)