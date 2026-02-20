from django.shortcuts import get_object_or_404
from . import models
from django.views import generic


class MyShopView(generic.ListView):
    model = models.Product
    template_name = "product.html"
    context_object_name = "products"



class CategoriesView(generic.ListView):
    model = models.Category
    template_name = "categories.html"
    context_object_name = "categories"



class CategoryProductsView(generic.ListView):
    model = models.Product
    template_name = "category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        self.category = get_object_or_404(models.Category, id=self.kwargs["id"])
        return self.category.products.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context