from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer,UserModelSerializer,INEModelSerializer,PassportModelSerializer
from .models import Bucketlist,UserModel,INEModel,PassportModel

class UserCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def perform_create(self, serializer):
        serializer.save()

class INECreateView(generics.ListCreateAPIView):
    queryset = INEModel.objects.all()
    serializer_class = INEModelSerializer

    def perform_create(self, serializer):
        serializer.save()

class PassportCreateView(generics.ListCreateAPIView):
    queryset = PassportModel.objects.all()
    serializer_class = PassportModelSerializer

    def perform_create(self, serializer):
        serializer.save()
