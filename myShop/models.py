from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name_product = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self):
        return f'{self.name_product} --- {self.category}'
    
