from django.urls import path
from . import views

urlpatterns = [
    # /api/products/
    path('products/', views.products_list, name='products-list'),

    # /api/products/<int:id>/
    path('products/<int:id>/', views.product_detail, name='product-detail'),

    # /api/categories/
    path('categories/', views.categories_list, name='categories-list'),

    # /api/categories/<int:id>/
    path('categories/<int:id>/', views.category_detail, name='category-detail'),

    # /api/categories/<int:id>/products/
    path('categories/<int:id>/products/', views.category_products, name='category-products'),
]
