from django.shortcuts import render

from .models import Products
# Create your views here.


def product_list(request):
    limit = int(request.GET.get('limit', 10))  # Get the selected limit from the query parameter, default to 10 if not provided
    products = Products.objects.all()[:limit]  # Retrieve the products based on the selected limit
    return render(request, 'product_list.html', {'products': products})


