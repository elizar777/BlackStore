from django.urls import path 
from apps.users.views import UserAPI, UserAPIDetail

urlpatterns = [
    path('users/', UserAPI.as_view(), name='api_user'),
    path('users/<int:pk>/', UserAPIDetail.as_view(), name='api_users_detail')
]
