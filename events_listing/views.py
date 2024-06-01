from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from .models import PostEvent, EventSignUp, Comment
from .forms import CommentForm, EventFilterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

class PostList(generic.ListView):
    template_name = "events_listing/index.html"
    paginate_by = 6

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = PostEvent.objects.filter(date__gte=current_datetime)
        
        query = self.request.GET.get('q')
        race_type = self.request.GET.get('race_type')
        location = self.request.GET.get('location')

        if query:
            # Search in PostEvent model
            queryset = queryset.filter(
                Q(event_name__icontains=query) |
                Q(description__icontains=query)
            )

            # Get IDs of matching objects from other models
            event_signup_ids = EventSignUp.objects.filter(
                Q(user__username__icontains=query) |
                Q(event__event_name__icontains=query) |
                Q(event__description__icontains=query)
            ).values_list('event_id', flat=True)

            comment_ids = Comment.objects.filter(
                Q(author__username__icontains=query) |
                Q(body__icontains=query)
            ).values_list('post_id', flat=True)

            # Filter PostEvent queryset based on IDs from other models
            queryset = queryset | PostEvent.objects.filter(id__in=event_signup_ids)
            queryset = queryset | PostEvent.objects.filter(id__in=comment_ids)
        
        if race_type:
            queryset = queryset.filter(race_type=race_type)

        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventFilterForm(self.request.GET or None)
        return context

def postevent_detail(request, slug):
    queryset = PostEvent.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
       
    # Pass the post object to the template context
    remaining_places = max(post.max_participants - post.signups.count(), 0)
    
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



        elif 'unregister' in request.POST:
            EventSignUp.objects.filter(event=post, user=request.user).delete()
            messages.add_message(request, messages.SUCCESS, 'You have unregistered from the event.')
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
            "remaining_places": remaining_places, 
        },
    )

def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = PostEvent.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('postevent_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    queryset = PostEvent.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('postevent_detail', args=[slug]))
