from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterView(APIView):
    def post(self, request):
        User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        return Response({"message": "Registered"})


class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )

        if user:
            return Response({"message": "Login successful"})

        return Response({"message": "Invalid credentials"})