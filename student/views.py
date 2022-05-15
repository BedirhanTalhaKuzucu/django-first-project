from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello')

def henry(request):
    return HttpResponse("MY NAME İS hENRY")