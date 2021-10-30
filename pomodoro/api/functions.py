from.models import Pomodoro, TimeSpent
import pandas
from datetime import timedelta

def get_pomodoros_specific_period(date_start,date_end,pomotree) -> dict:
    pomodoros = Pomodoro.objects.filter(created_at__range=(date_start,date_end),pomodorotree_id=pomotree.id).values()
    all_dates = pandas.date_range(date_start+timedelta(days=1),date_end,freq='d')
    
    pomodoro_per_day = {}
    for date in all_dates:
        pomodoro_per_day[date.strftime("%Y-%m-%d")] = 0

    for pomodoro in pomodoros:
        day = pomodoro['created_at'].strftime("%Y-%m-%d")
        if day in pomodoro_per_day:
            pomodoro_per_day[day]+=1
    
    return pomodoro_per_day

def get_time_spent_period(date_start,date_end,pomotree):
    time_entries = TimeSpent.objects.filter(date__range=(date_start,date_end),pomodorotree_id=pomotree.id).values()
    all_dates = pandas.date_range(date_start+timedelta(days=1),date_end,freq='d')
    
    time_per_day = {}
    for date in all_dates:
        time_per_day[date.strftime("%Y-%m-%d")] = 0
    
    for time in time_entries:
        day = time['date'].strftime("%Y-%m-%d") 
        if day in time_per_day:
            time_per_day[day] += int(time['time_spent'])

    return time_per_day