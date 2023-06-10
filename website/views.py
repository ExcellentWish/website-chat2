from django.shortcuts import render
from django.conf import settings
from django.views import View

# Create your views here.

def index(request):
    # Return homepage
    return render(request, 'index.html')

def page1(request):
    # Return otherpage
    return render(request, 'page.html')


def page2(request):
    # Return otherpage
    return render(request, 'page1.html')

def page3(request):
    # Return otherpage
    return render(request, 'page2.html')
