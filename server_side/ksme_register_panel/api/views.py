from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


from .serializers import UserSerializer , Level1Serializer, Level2Serializer, Level3Serializer


class UsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_data = UserSerializer(users, many=True)

        return Response(serialized_data.data)


class Level1(APIView):
    def post(self, request):

        serializer = Level1Serializer(data=request.data)

        try:
            if serializer.is_valid():
                return Response(True, status=200)

            else:
                return Response(serializer.errors, status=400)
        except:
            context = {
                'server error': 'An error has occured on the server'
            }
            return Response(context, status=500)



class Level2(APIView):
    def post(self, request):

        serializer = Level2Serializer(data = request.data)

        try:
            if serializer.is_valid():
                return Response(True, status=200)

            else:
                return Response(serializer.errors, status=400)
        except:
            context = {
                'server error': 'An error has occured on the server'
            }
            return Response(context, status=500)


class Level3(APIView):
    def post(self, request):

        serializer = Level3Serializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(True, status=200)
        else:
            return Response(serializer.errors, status=400)

        # try:
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(True, status=200)
        #     else:
        #         return Response(serializer.errors, status=400)
        # except:
        #     context = {
        #         'server error': 'An error has occured on the server'
        #     }
        #     return Response(context, status=500)

