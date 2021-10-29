from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class PomodoroTree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_pomodors = models.IntegerField()
    time_for_next_pomodoro = models.TimeField() 

class Pomodoro(models.Model):
    pomodotree = models.ForeignKey(PomodoroTree,on_delete=models.CASCADE)
    create_ad = models.DateField(auto_now_add=True)

class TimeSpent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_spent = models.TimeField()

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()

class RedeemedRewards(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    reward = models.ForeignKey(Reward, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)