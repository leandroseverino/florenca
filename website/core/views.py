from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    output = 'Ola Mundo'
    return render(request, 'index.html')
