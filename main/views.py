from django.http import HttpResponse, request
from django.shortcuts import render

def index(request: request):
    return render(request, 'main/index.html')

def about(request: request):
   context = {
       'content': 'About Us',
       'text_on_page': 'Best market exist.'
   }
   return render(request, 'main/about.html', context)
