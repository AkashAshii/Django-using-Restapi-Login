from rest_framework.response import Response
from . models import Person
from . serializers import PersonSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonSerializer
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.contrib.auth.hashers import check_password
from . import backends

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListLoginRegAPIView(APIView):
    def get(self,request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

class UserLoginAPIView(APIView,backends.PersonAuthBackend):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if user is not None:
            person = Person.objects.get(username=user.username)
            serializer = PersonSerializer(person, many=False)#django model is converted into json
            return Response({'detail': 'User found with the given username and password.','user': serializer.data}, status=200)
        else:
            return Response({'detail': 'User not found with the given username and password.'}, status=404)


