from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['POST'])
def add_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if not  all([username,password,email]):
        raise Exception('erro')

    new_user = User.objects.create_user(username=username,email=email,password=password)
    
    serialized_user = UserSerializer(new_user).data

    return Response({'user':serialized_user})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serialized_user = UserSerializer(user,many=True).data

    return Response({'user':serialized_user})


