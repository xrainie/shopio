from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.core.cache import cache


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    all_products = cache.get('all_products')
    if not all_products:
        all_products = Product.objects.filter(available=True)
        cache.set('all_products', all_products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        key = f'category_{category.id}_products'
        products = cache.get(key)
        if not products:
            products = all_products.filter(category=category)
            cache.set(key, products)
    else: 
        products = all_products

    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
