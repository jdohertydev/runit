from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import PostEvent

# Create your views here.

# def my_events_listing(request):
#     return HttpResponse("Hello, Runners!")

class PostList(generic.ListView):
    queryset = PostEvent.objects.all()
    template_name = "events_listing/post_list.html"  # Ensure this matches the path to your template