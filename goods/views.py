from django.http import request
from django.shortcuts import render

from goods.models import Products


def catalog(request: request):
    goods = Products.objects.all()

    context = {
        "title": "Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request: request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context)
