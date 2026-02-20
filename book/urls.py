from django.urls import path
from . import views

app_name='library'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_search'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name="book_detail"),
    path('books/<int:id>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name='update_book'),
    path('create_book/', views.BookCreateView.as_view(), name='create_book'),

   
]