from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'inscription/index.html')

def contact(request):
    return render(request, 'inscription/contact.html')

def inscription(request):
    return render(request, 'inscription/inscription.html')

def apropos(request):
    return render(request, 'inscription/apropos.html')


