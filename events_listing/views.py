# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import generic
# from django.contrib import messages
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
# from .models import PostEvent, EventSignUp, Comment
# from .forms import CommentForm

# class PostList(generic.ListView):
#     template_name = "events_listing/index.html"
#     paginate_by = 6

#     def get_queryset(self):
#         current_datetime = timezone.now()
#         queryset = PostEvent.objects.filter(date__gte=current_datetime)
#         return queryset

# def postevent_detail(request, slug):
#     queryset = PostEvent.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)
#     comments = post.comments.all().order_by("-created_on")
#     comment_count = post.comments.filter(approved=True).count()
    
    
#     if request.method == "POST":
#         if 'comment_form' in request.POST:
#             comment_form = CommentForm(request.POST)
#             if comment_form.is_valid():
#                 comment = comment_form.save(commit=False)
#                 comment.author = request.user
#                 comment.post = post
#                 comment.save()
#                 messages.success(request, 'Comment submitted and awaiting approval')
#                 return redirect('post-detail', slug=post.slug)
#             else:
#                 messages.error(request, 'Error submitting comment. Please check the form.')
#         elif 'signup' in request.POST:
#             signup, created = EventSignUp.objects.get_or_create(event=post, user=request.user)
#             if created:
#                 messages.success(request, 'You have successfully signed up for this event.')
#             else:
#                 messages.info(request, 'You are already signed up for this event.')
#         elif 'unsubscribe' in request.POST:
#             EventSignUp.objects.filter(event=post, user=request.user).delete()
#             messages.success(request, 'You have unsubscribed from this event.')

#     comment_form = CommentForm()
#     user_signed_up = request.user.is_authenticated and EventSignUp.objects.filter(event=post, user=request.user).exists()
#     signups = EventSignUp.objects.filter(event=post)

#     return render(
#         request,
#         "events_listing/postevent_detail.html",
#         {
#             "post": post,
#             "comments": comments,
#             "comment_count": comment_count,
#             "comment_form": comment_form,
#             "user_signed_up": user_signed_up,
#             "signups": signups,  # Pass signups to the template
#         },
#     )

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from .models import PostEvent, EventSignUp, Comment
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
    
    # Check if the user is signed up for the event
    user_signed_up = request.user.is_authenticated and EventSignUp.objects.filter(event=post, user=request.user).exists()

    comment_form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        if 'signup' in request.POST:
            if post.signups.count() < post.max_participants:
                EventSignUp.objects.create(event=post, user=request.user)
                messages.add_message(request, messages.SUCCESS, 'You have signed up for the event.')
            else:
                messages.add_message(request, messages.ERROR, 'The event is full.')
            return redirect('postevent_detail', slug=post.slug)
        elif 'unsubscribe' in request.POST:
            EventSignUp.objects.filter(event=post, user=request.user).delete()
            messages.add_message(request, messages.SUCCESS, 'You have unsubscribed from the event.')
            return redirect('postevent_detail', slug=post.slug)
        else:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
                return redirect('postevent_detail', slug=post.slug)

    return render(
        request,
        "events_listing/postevent_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_signed_up": user_signed_up,
            "signups": post.signups.all(),
        },
    )