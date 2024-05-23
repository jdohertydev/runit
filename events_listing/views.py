from django.shortcuts import render
from django.views import generic
from .models import PostEvent

# Create your views here.

class PostList(generic.ListView):
    queryset = PostEvent.objects.all()
    template_name = "events_listing/index.html"
    paginate_by = 6