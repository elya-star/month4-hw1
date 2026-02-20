from django.urls import path
from . import views

urlpatterns = [
    path('all_users/', views.RelationDBView.as_view()),
]