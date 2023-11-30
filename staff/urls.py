# staff/urls.py
from django.urls import path
from .views import register_staff,login_view,home

urlpatterns = [
    path('register/', register_staff, name='register_staff'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),

]
