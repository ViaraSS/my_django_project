from django.http import HttpResponse
from django.shortcuts import render


def homePageView(request):
    return HttpResponse('Hello, World!')


def home_view(request):
    return render(request, 'pages/home.html')
