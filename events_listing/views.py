from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from .models import PostEvent
from .forms import CommentForm

class PostList(generic.ListView):
    template_name = "events_listing/index.html"
    paginate_by = 6

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = PostEvent.objects.filter(date__gte=current_datetime)
        return queryset

def postevent_detail(request, slug):
    queryset = PostEvent.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    comment_form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            # Redirect to avoid form resubmission
            return redirect('post-detail', slug=post.slug)
        else:
            messages.error(request, 'Error submitting comment. Please check the form.')
    
    return render(
        request,
        "events_listing/postevent_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
