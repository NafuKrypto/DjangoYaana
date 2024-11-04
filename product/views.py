

from django.shortcuts import render
from django.views.generic import ListView

from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    # ct = 'products'
    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data()
    #     return ctx
    def get_queryset(self):
        queryset= super().get_queryset()
        # filtered_data = c.filter(unit_price__lte=4.50)
        # self.queryset = filtered_data
        name = self.request.GET.get('name')

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return  queryset