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

@api_view(['POST'])
def registerService(request):
    if request.method == "GET":
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        guaaranteMonths = 0
        client_name = request.data.get('client_name')
        client_contact = request.data.get('client_contact')
        head_model = request.data.get('head_model')
        start_date = request.data.get('start_date')
        order_of_service = request.data.get('order_of_service')
        guarantee = request.data.get('guarantee')
        grind = request.data.get('grind')
        weld = request.data.get('weld')
        pleinar = request.data.get('pleinar')
        to_wash = request.data.get('to_wash')
        washclean_valves = request.data.get('washclean_valves')
        to_polish = request.data.get('to_polish')

        if guarantee: guaaranteMonths = 3

        register_service = Services.objects.create(
            client_name=client_name,
            client_contact=client_contact,
            head_model=head_model,
            start_date=start_date,
            order_of_service=order_of_service,
            guarantee=guaaranteMonths,
            grind=grind,
            weld=weld,
            pleinar=pleinar,
            to_wash=to_wash,
            washclean_valves=washclean_valves,
            to_polish=to_polish
        )
        register_service.save()

        return Response("Serviço registrado com sucesso!", status=status.HTTP_201_CREATED)

@api_view(['GET'])
def filterService(request, query):
    service = Services.objects.filter(order_of_service__icontains=query)
    serialized_service = ServiceSerializer(service, many=True)
    if not serialized_service:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serialized_service.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def logout(request):
    logout_django(request)
    return Response('Usúario deslogado', status=status.HTTP_200_OK)