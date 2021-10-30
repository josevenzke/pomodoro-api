from django.urls import path
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-userinfo/', views.get_user, name='user-info'),
    path('create-user/',views.add_user,name='create-user'),
    path('add-time/', views.add_time, name='add-time'),
    path('get-pomodoros-data/', views.get_pomodoros, name='get-pomodoro-data'),
    path('get-timespent-data/', views.get_time_spent,name='get-timespent-data'),
    path('add-reward/', views.add_reward, name='add-reward'),
    path('get-rewards/', views.get_rewards, name='get-rewards'),
    path('buy-reward/<int:id_>/', views.buy_reward, name='buy-reward')
]