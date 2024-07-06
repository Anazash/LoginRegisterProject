from django.urls import path
from .views import register, user_login, home

urlpatterns = [
    path('', register, name='register'),
    path('login/', user_login, name='login'),
    path('home', home, name='home'),
]
