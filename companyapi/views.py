from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .serializer import UserSerializer, GroupSerializer, CompanyUserSerializer
from rest_framework import permissions, viewsets, parsers
from .models import CompanyUsers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
@csrf_exempt
def company_user_list(request):
    if request.method == 'GET':
        company_users = CompanyUsers.objects.all()
        serializer = CompanyUserSerializer(company_users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        serializer = CompanyUserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def company_user_detail(request, pk):
    try:
        objects = CompanyUsers.objects.get(pk=pk)
    except CompanyUsers.DoesNotExist:
        return JsonResponse(status=404)
    if request.method == 'GET':
        serializer = CompanyUserSerializer(objects)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        data = parsers.JSONParser().parse(request)
        serializer = CompanyUserSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    if request.method == 'DELETE':
        objects.delete()
        return JsonResponse(status=204)
        