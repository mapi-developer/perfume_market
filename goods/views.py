from django.http import request
from django.shortcuts import render

from goods.models import Categories, Products


def catalog(request: request):
    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        "title": "Catalog",
        "goods": goods,
        'categories': categories,
    }
    return render(request, "goods/catalog.html", context)


def product(request: request):
    return render(request, "goods/product.html")
