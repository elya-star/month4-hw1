from django.urls import path
from . import views

urlpatterns = [
    path('my_shop/', views.myShop),
    path('categories/', views.categories_view),
    path('category/<int:id>/', views.category_products_view),
]