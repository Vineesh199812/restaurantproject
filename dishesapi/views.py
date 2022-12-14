from django.shortcuts import render

# Create your views here.

from dishesapi.models import Dishes,Reviews
from rest_framework.views import APIView
from rest_framework.response import Response
from dishesapi.serializers import DishesSerializer,DishesModelSerializer,UserSerializer,ReviewSerializer
from rest_framework import status,viewsets
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action

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

class DishesModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=DishesModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=DishesModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class DishesDetailModelView(APIView):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("id")
        try:
            qs=Dishes.objects.get(id=id)
            serializer=DishesModelSerializer(qs)
            return Response(data=serializer.data)
        except:
            return Response({"msg":"doesn't exist"},status=status.HTTP_404_NOT_FOUND)
    def put(self,req,*args,**kwargs):
        id=kwargs.get("id")
        try:
            instance=Dishes.objects.get(id=id)
            serializer=DishesModelSerializer(data=req.data,instance=instance)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        except:
            return Response({"msg":"doesn't exist"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,req,*args,**kwargs):
        id=kwargs.get("id")
        try:
            qs=Dishes.objects.get(id=id)
            qs.delete()
            return Response({"msg":"deleted"})
        except:
            return Response({"msg":"doesn't exist"},status=status.HTTP_404_NOT_FOUND)

class DishesViewSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=DishesModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        serializer=DishesModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")    # pk ==> primary key(instead of id)
        object=Dishes.objects.get(id=id)
        serializer=DishesModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Dishes.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)

    def retrieve(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        object=Dishes.objects.get(id=id)
        serializer=DishesModelSerializer(object)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class DishesModelViewSetView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = DishesModelSerializer
    queryset = Dishes.objects.all()

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        dish=Dishes.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"dish":dish})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class UserRegistrationView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()