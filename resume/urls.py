from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.auth_login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.auth_logout_view, name='logout'),
]