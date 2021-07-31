from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .serializers import UserSerializer
from .serializers import Level1Serializer

class UsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_data = UserSerializer(users, many=True)

        return Response(serialized_data.data)


class Level1(APIView):
    def post(self, request):

        serializer = Level1Serializer(data=request.data)
        if serializer.is_valid():
            return Response(True, status=200)

        else:
            return Response(serializer.errors, status=400)

