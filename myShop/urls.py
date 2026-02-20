from django.urls import path
from . import views

urlpatterns = [
    path('my_shop/', views.MyShopView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('category/<int:id>/', views.CategoryProductsView.as_view()),
]