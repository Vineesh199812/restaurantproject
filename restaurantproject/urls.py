"""restaurantproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dishesapi import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v3/restaurant/dishes",views.DishesViewSetView,basename="dishes")
router.register("api/v4/restaurant/dishes",views.DishesModelViewSetView,basename="dishes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/restaurant/dishes/',views.DishesView.as_view()),
    path('api/v1/restaurant/dishes/<int:id>',views.DishesDetailView.as_view()),
    path('api/v2/restaurant/dishes/',views.DishesModelView.as_view()),
    path('api/v2/restaurant/dishes/<int:id>',views.DishesDetailModelView.as_view()),
]+router.urls
