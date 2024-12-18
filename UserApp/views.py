from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema

#@swagger_auto_schema(request_body=UserSerializer, method='post')

@api_view(['GET'])
def GetUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
    
@transaction.atomic
@api_view(['POST'])
def AddUser(request, username, password):
    data = {'username': username, 'password': password}
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@transaction.atomic
@api_view(['PUT'])
def EditUser(request, user_id, username, password):
    try:
        user_instance = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"Error":"User not found"}, status=404)
    data = {'username': username, 'password': password}
    serializer = UserSerializer(user_instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@transaction.atomic
@api_view(['DELETE'])
def DeleteUser(request, user_id):
    try:
        user_instance = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error":"User no found"}, status=404)
    
    user_instance.delete()
    return Response({"message":"User Deleted Successfully"})
