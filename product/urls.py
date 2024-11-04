from django.urls import path

from product.views import ProductListView

urlpatterns = [
    path('lists', ProductListView.as_view(), name='product-list'),

]
