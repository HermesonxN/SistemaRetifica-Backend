from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['POST'])
def login(request):
    if request.method == "GET":
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return Response('Usúario logado com sucesso!', status=status.HTTP_200_OK)
        else:
            return Response('Usúario e/ou senha incorretos!', status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def logout(request):
    logout_django(request)
    return Response('Usúario deslogado', status=status.HTTP_200_OK)