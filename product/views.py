
from django.views.generic import ListView

from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        queryset= super().get_queryset()

        name = self.request.GET.get('name')

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return  queryset