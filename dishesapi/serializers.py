

from rest_framework import serializers

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