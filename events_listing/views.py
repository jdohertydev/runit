from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import PostEvent

class PostList(generic.ListView):
    template_name = "events_listing/index.html"
    paginate_by = 6

    def get_queryset(self):
        # Get the current date and time
        current_datetime = timezone.now()
        
        # Filter the queryset to include only events whose date is greater than or equal to the current date and time
        queryset = PostEvent.objects.filter(date__gte=current_datetime)

        return queryset