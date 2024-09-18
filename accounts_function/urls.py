from django.urls import path
from .views import register, home, login, logout


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
]
