from django.shortcuts import render, get_object_or_404
from . import models

def myShop(request):
    if request.method == "GET":
        products = models.Product.objects.all()
        return render(
            request,
            "product.html",
            {
                "products": products
            }
        )
    
def categories_view(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        return render(
            request,
            "categories.html",
            {
                "categories": categories
            }
        )
    
def category_products_view(request, id):
    category = get_object_or_404(models.Category, id=id)
    products = category.products.all()
    return render(
        request,
        "category_products.html",
        {
            "category": category,
            "products": products
        }
    )
# Create your views here.
