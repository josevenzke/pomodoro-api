from django.urls import path
from api import views


urlpatterns = [
    path('get-userinfo/', views.get_user, name='user-info'),
    path('create-user/',views.add_user,name='create-user'),
    path('add-time/', views.add_time, name='add-time'),
    path('get-pomodoros-data/', views.get_pomodoros, name='get-pomodoro-data'),
    path('get-timespent-data/', views.get_time_spent,name='get-timespent-data'),
    path('add-reward/', views.add_reward, name='add-reward'),
    path('get-rewards/', views.get_rewards, name='get-rewards'),
    path('buy-reward/<int:id_>/', views.buy_reward, name='buy-reward')
]