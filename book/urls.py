from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
    path('books/<int:id>/delete/', views.delete_book_view),
    path('books/<int:id>/update/', views.update_book_view),
    path('create_book/', views.create_book_view),
   
]