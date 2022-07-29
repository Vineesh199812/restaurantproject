

from rest_framework import serializers
from dishesapi.models import Dishes

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