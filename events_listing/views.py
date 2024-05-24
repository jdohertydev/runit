from django.shortcuts import render, get_object_or_404
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

def postevent_detail(request, slug):
    """
    Display an individual :model:`events_listing.PostEvent`.

    **Context**

    ``post``
        An instance of :model:`events_listing.PostEvent`.

    **Template:**

    :template:`events_listing/postevent_detail.html`
    """

    queryset = PostEvent.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "events_listing/postevent_detail.html",
        {"post": post},
    )
