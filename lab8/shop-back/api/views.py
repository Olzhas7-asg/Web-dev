import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product, Category


def product_to_dict(product):
    """Конвертирует объект Product в словарь для JSON-ответа."""
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category': {
            'id': product.category.id,
            'name': product.category.name,
        }
    }


def category_to_dict(category):
    """Конвертирует объект Category в словарь для JSON-ответа."""
    return {
        'id': category.id,
        'name': category.name,
    }


# GET /api/products/
@require_http_methods(['GET'])
def products_list(request):
    """Возвращает список всех продуктов."""
    products = Product.objects.select_related('category').all()
    data = [product_to_dict(p) for p in products]
    return JsonResponse(data, safe=False)


# GET /api/products/<int:id>/
@require_http_methods(['GET'])
def product_detail(request, id):
    """Возвращает один продукт по ID."""
    try:
        product = Product.objects.select_related('category').get(id=id)
        return JsonResponse(product_to_dict(product))
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


# GET /api/categories/
@require_http_methods(['GET'])
def categories_list(request):
    """Возвращает список всех категорий."""
    categories = Category.objects.all()
    data = [category_to_dict(c) for c in categories]
    return JsonResponse(data, safe=False)


# GET /api/categories/<int:id>/
@require_http_methods(['GET'])
def category_detail(request, id):
    """Возвращает одну категорию по ID."""
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category_to_dict(category))
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)


# GET /api/categories/<int:id>/products/
@require_http_methods(['GET'])
def category_products(request, id):
    """Возвращает все продукты конкретной категории."""
    try:
        category = Category.objects.get(id=id)
        products = Product.objects.select_related('category').filter(category=category)
        data = [product_to_dict(p) for p in products]
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
