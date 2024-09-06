from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    return render(request, 'contacts.html')


def home(request):
    return render(request, 'home.html')


def products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

