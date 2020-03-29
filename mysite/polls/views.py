from django.http.request import HttpRequest
from django.http.response import JsonResponse, HttpResponse
from .models import Product, Category
from django.db.models import F


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'message does not exits'})
    return JsonResponse(product.to_json())


def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 404})
    return JsonResponse(category.to_json())


def category_all(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 404})

    products = category.product_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products.to_json())
