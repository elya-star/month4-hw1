from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.core.paginator import Paginator

def search_book_view(request):
    query = request.GET.get("s", '')
    all_books = models.Books.objects.all().order_by('id')
    if query:
        books = [b for b in all_books if query in b.title.lower()]
    else:
        books = all_books
    paginator = Paginator(books, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'book_list.html',
        {
             "page_obj": page_obj,
             "query": query,
        }

    )


#UPDATE BOOK
def update_book_view(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    if request.method == "POST":
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = forms.BookForm(instance=book_id)
    return render(
        request,
        "update_book.html",
        {
            "form": form,
            "book_id": book_id
        }
    )

#DELETE BOOK
def delete_book_view(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    book_id.delete()
    return redirect('/book_list/')

#CREATE BOOK
def create_book_view(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = forms.BookForm()
        
    return render(
        request,
        "create_book.html",
        {
            "form": form
        }
    )

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
        books = models.Books.objects.all()
        paginator = Paginator(books, 2)  
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "book_list.html",
            {
                "page_obj": page_obj
            }
        )

