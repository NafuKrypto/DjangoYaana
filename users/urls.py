from django.urls import path

from users.views import UserLogin

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
]