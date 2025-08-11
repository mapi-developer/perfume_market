from django.http import request
from django.shortcuts import render

from goods.models import Categories

def index(request: request):
    categories = Categories.objects.all()

    context = {
       'categories': categories,
   }

    return render(request, 'main/index.html', context)

def about(request: request):
   context = {
       'content': 'About Us',
       'text_on_page': 'Best market exist.',
   }
   return render(request, 'main/about.html', context)
