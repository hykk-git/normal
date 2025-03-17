from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('board/', board_view, name='board'),
    path('board/new/', create_post_view, name='create_post'),
]