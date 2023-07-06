from django.shortcuts import render
from django.http import JsonResponse
from .models import Products
# Create your views here.


def product_list(request):
    # limit = int(request.GET.get('limit', 10))  # Get the selected limit from the query parameter, default to 10 if not provided
    # products = Products.objects.all()  # Retrieve the products based on the selected limit
    return render(request, 'product_list.html')


def product_api(request):
    products = Products.objects.all().values()
    return JsonResponse({"products": list(products)})


