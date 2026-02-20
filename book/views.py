from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic

# SEARCH + LIST BOOKS
class BookListView(generic.ListView):
    model = models.Books
    template_name = "book_list.html"
    context_object_name = "page_obj"
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get("s", "")
        all_books = models.Books.objects.all().order_by("id")

        if query: 
            books = [b for b in all_books if query.lower() in b.title.lower()] 
            return books 
        return all_books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("s", "")
        return context


        

# def search_book_view(request):
#     query = request.GET.get("s", '')
#     all_books = models.Books.objects.all().order_by('id')
#     if query:
#         books = [b for b in all_books if query in b.title.lower()]
#     else:
#         books = all_books
#     paginator = Paginator(books, 2)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(
#         request,
#         'book_list.html',
#         {
#              "page_obj": page_obj,
#              "query": query,
#         }

#     )


#UPDATE BOOK

class BookUpdateView(generic.UpdateView):
    model = models.Books
    form_class = forms.BookForm
    template_name = "update_book.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("library:book_search")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_id"] = self.object
        return context
    
# def update_book_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/books/')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(
#         request,
#         "update_book.html",
#         {
#             "form": form,
#             "book_id": book_id
#         }
#     )

#DELETE BOOK

class BookDeleteView(generic.DeleteView):
    model = models.Books
    template_name = "delete_book.html"
    success_url = reverse_lazy("library:book_search")
    pk_url_kwarg = "id"

    

# def delete_book_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     book_id.delete()
#     return redirect('/book_list/')

#CREATE BOOK

class BookCreateView(generic.CreateView):
    model = models.Books
    form_class = forms.BookForm
    template_name = "create_book.html"
    success_url = reverse_lazy("library:book_search")

# def create_book_view(request):
#     if request.method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/books/')
#     else:
#         form = forms.BookForm()
        
#     return render(
#         request,
#         "create_book.html",
#         {
#             "form": form
#         }
#     )


class BookDetailView(generic.DetailView):
    model = models.Books
    template_name = "book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"

# def book_detail(request, id):
#     if request.method == 'GET':
#         book = get_object_or_404(models.Books, id=id)
#         return render(
#             request,
#             'book_detail.html',
#             {
#                 "book": book
#             }
#         )




# def book_list(request):
#     if request.method == "GET":
#         books = models.Books.objects.all()
#         paginator = Paginator(books, 2)  
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)

#         return render(
#             request,
#             "book_list.html",
#             {
#                 "page_obj": page_obj
#             }
#         )

