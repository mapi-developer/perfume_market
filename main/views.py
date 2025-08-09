from django.http import HttpResponse, request
from django.shortcuts import render

def index(request: request):
    context = {
        'title': 'Home',
        'content': 'Market Main Page',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True,
    }

    return render(request, 'main/index.html', context)

def about(request: request):
    return HttpResponse('About page')
