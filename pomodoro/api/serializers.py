from api.models import PomodoroTree
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','date_joined']

class PomodoroTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroTree
        fields = ['id','user','all_time_pomodoros','current_pomodoros','next_pomodoro']

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id','name','description','cost']