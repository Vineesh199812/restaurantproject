from django.shortcuts import render

# Create your views here.

from dishesapi.models import Dishes
from rest_framework.views import APIView
from rest_framework.response import Response
from dishesapi.serializers import DishesSerializer
from rest_framework import status

#url: restaurant/dishes/
#get: to get all the dishes
#post: to add a dish

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=DishesSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=DishesSerializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

#url: restaurant/dishes/{id}
class DishesDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            qs=Dishes.objects.get(id=id)
            serializer=DishesSerializer(qs)
            return Response(data=serializer.data)
        except:
            return Response({"msg":"doesn't exist"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            object=Dishes.objects.get(id=id)
            serializer=DishesSerializer(data=request.data)
            if serializer.is_valid():
                object.dishname=serializer.validated_data.get("dishname")
                object.price=serializer.validated_data.get("price")
                object.category=serializer.validated_data.get("category")
                object.save()
                return Response(data=serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"msg":"doesn't exist"},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            object=Dishes.objects.get(id=id)
            object.delete()
            return Response({"msg":"deleted"})
        except:
            return Response({"msg":"doesn't exist"},status=status.HTTP_404_NOT_FOUND)