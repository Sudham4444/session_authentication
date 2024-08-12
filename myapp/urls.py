from django.urls import path
from .views import home, user_login, user_logout, user_list, register

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/users/', user_list, name='user-list'),
    path('register/', register, name='register'),
]
