from django.shortcuts import render
from .models import Food,FoodType,Comment
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .serializers import FoodSerializers,FoodTypeSerializers,CommentSerializers
from  rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly)


class FoodTypeApiViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class FoodApiViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]