from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class HomeView(TemplateView):
    template_name = 'home.html'

# Код, который был заменён лежит внизу.

# def home(request):
#     return render(request, 'home.html')


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#
#     return render(request, 'contacts.html')


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'product_detail.html', context)


# def products(request):
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, 'blog_list.html', context)
