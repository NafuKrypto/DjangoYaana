

from django.shortcuts import render
from django.views.generic import ListView

from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    # ct = 'products'