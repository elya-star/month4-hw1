from django.shortcuts import render, get_object_or_404
from . import models


def book_detail(request, id):
    if request.method == 'GET':
        book = get_object_or_404(models.Books, id=id)
        return render(
            request,
            'book_detail.html',
            {
                "book": book
            }
        )


def book_list(request):
    if request.method == "GET":
        book = models.Books.objects.all()
        return render(
            request, 
            'book_list.html',
            {
                "book": book
            } 
        )
