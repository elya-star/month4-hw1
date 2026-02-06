from django.urls import path
from . import views

urlpatterns = [
    path('all_users/', views.relation_db)
]