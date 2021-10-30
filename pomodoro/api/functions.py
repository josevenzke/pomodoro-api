from.models import Pomodoro, TimeSpent
import pandas
from datetime import timedelta
import datetime

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

def get_day_streak(pomodoro_tree):
    total_streak = 0
    current_streak = 0
    today = datetime.date.today()
    compareDate = today + datetime.timedelta(1) # Tomorrow

    time_spent = TimeSpent.objects.filter(pomodorotree=pomodoro_tree, date__lte = today).order_by("-date")

    for time in time_spent:
        # Get the difference btw the dates

        delta = compareDate - time.date

        if delta.days == 1: # Keep the streak going!
            current_streak += 1
        elif delta.days == 0: # Don't bother increasing the day if there's multiple ones on the same day
            pass
        else: # Awwww...
            break # The current streak is done, exit the loop

        compareDate = time.date

    if current_streak > total_streak:
        total_streak = current_streak

    return total_streak