from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Food,FoodType,Comment
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .serializers import FoodSerializers,FoodTypeSerializers,CommentSerializers
from  rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly)
from rest_framework.authentication import TokenAuthentication

class FoodTypeApiViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes =[TokenAuthentication]

class FoodApiViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [TokenAuthentication]

class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [TokenAuthentication]

class FoodApiList(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]