from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView


from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/blog_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


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
