from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def base(request):
    return HttpResponse('Hello Base Here')
