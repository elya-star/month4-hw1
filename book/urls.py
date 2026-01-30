from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.favorite_quote_view),
]