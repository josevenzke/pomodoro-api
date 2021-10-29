from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from .serializers import *
from .models import PomodoroTree
from django.contrib.auth.models import User

import datetime
from datetime import timedelta
from .functions import *

# Create your views here.
@api_view(['POST'])
def add_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if not  all([username,password,email]):
        raise Exception('erro')

    new_user = User.objects.create_user(username=username,email=email,password=password)

    new_pomodorotree = PomodoroTree.objects.create(user=new_user)

    serialized_user = UserSerializer(new_user).data
    serialized_pomodorotree = PomodoroTreeSerializer(new_pomodorotree).data

    return Response({'user':serialized_user,'pomodoro_tree':serialized_pomodorotree})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serialized_user = UserSerializer(user).data

    return Response({'user':serialized_user})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_time(request):
    time = request.POST.get('time')

    pomotree = PomodoroTree.objects.get(user=request.user)
    pomotree.time_for_next_pomodoro += int(time)

    if pomotree.time_for_next_pomodoro >= 90:
        Pomodoro.objects.create(pomodotree=pomotree)
        pomotree.current_pomodoros += 1
        pomotree.all_time_pomodoros +=1
        pomotree.time_for_next_pomodoro -= 90
    
    pomotree.save()

    pomo = PomodoroTreeSerializer(pomotree).data
    return Response({'pomotree':pomo})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_pomodoros(request):
    time_period = request.POST.get('period')

    if time_period == 'week':
        date_end = datetime.date.today()
        date_start = date_end - timedelta(days=7)
        pomodoros = get_pomodoros_specific_period(date_start,date_end)
        #helper

    elif time_period == 'month':
        date_end = datetime.date.today()
        date_start = date_end - timedelta(days=30)
        pomodoros = get_pomodoros_specific_period(date_start,date_end)

    return Response({'pomodoros':pomodoros})










