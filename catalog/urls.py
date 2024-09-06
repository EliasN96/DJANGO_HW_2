from django.urls import path
from catalog.views import contacts, home, products, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]