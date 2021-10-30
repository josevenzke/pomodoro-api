from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class PomodoroTree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    all_time_pomodoros = models.IntegerField(default=0)
    current_pomodoros = models.IntegerField(default=0)
    time_for_next_pomodoro = models.IntegerField(default=0) 

class Pomodoro(models.Model):
    pomodorotree = models.ForeignKey(PomodoroTree,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

class TimeSpent(models.Model):
    pomodorotree = models.ForeignKey(PomodoroTree,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_spent = models.IntegerField()

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()

class SecretReward(models.Model):
    reward = models.ForeignKey(Reward,on_delete=models.CASCADE)
    content = models.TextField()
