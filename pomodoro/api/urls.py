from django.urls import path
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-user/', views.get_user),
    path('add-user/',views.add_user),
    path('add-time/', views.add_time),
    path('get-pomodoros/', views.get_pomodoros),
    path('get-timespent/', views.get_time_spent),
    path('add-reward/', views.add_reward),
    path('get-rewards/', views.get_rewards)
]