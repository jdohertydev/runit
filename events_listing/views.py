from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_events_listing(request):
    return HttpResponse("Hello, Runners!")