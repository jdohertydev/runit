from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.utils import timezone
from .models import PostEvent, EventSignUp, Comment
from .forms import CommentForm, EventFilterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .utils import send_signup_confirmation_email, send_unregistration_confirmation_email

def landing_page(request):
    return render(request, 'events_listing/landing_page.html')

def events_listing(request):
    return render(request, 'events_listing/index.html')

class PostList(generic.ListView):
    """
    View to display a list of post events with optional filtering.
    """

    template_name = "events_listing/index.html"
    paginate_by = 6

    def get_queryset(self):
        """
        Get the queryset for the list of post events.
        """
        current_datetime = timezone.now()
        queryset = PostEvent.objects.filter(date__gte=current_datetime)
        
        query = self.request.GET.get('q')
        race_type = self.request.GET.get('race_type')
        location = self.request.GET.get('location')

        if query:
            queryset = queryset.filter(
                Q(event_name__icontains=query) |
                Q(description__icontains=query) |
                Q(author__username__icontains=query)
            )

            event_signup_ids = EventSignUp.objects.filter(
                Q(user__username__icontains=query) |
                Q(event__event_name__icontains=query) |
                Q(event__description__icontains=query)
            ).values_list('event_id', flat=True)

            comment_ids = Comment.objects.filter(
                Q(author__username__icontains=query) |
                Q(body__icontains=query)
            ).values_list('post_id', flat=True)

            queryset = queryset | PostEvent.objects.filter(id__in=event_signup_ids)
            queryset = queryset | PostEvent.objects.filter(id__in=comment_ids)
        
        if race_type:
            queryset = queryset.filter(race_type=race_type)

        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Get the context data for the list of post events.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = EventFilterForm(self.request.GET or None)
        return context

class PostEventDetailView(View):
    """
    View to display the details of a post event.
    """
    def get(self, request, slug):
        """
        Handle GET requests to display the post event details.
        """
        post = get_object_or_404(PostEvent, slug=slug, status=1)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        remaining_places = max(post.max_participants - post.signups.count(), 0)
        user_signed_up = request.user.is_authenticated and EventSignUp.objects.filter(event=post, user=request.user).exists()
        comment_form = CommentForm()

        event_finished = post.date < timezone.now()
        signups = post.signups.all().order_by('signed_up_on')

        context = {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_signed_up": user_signed_up,
            "signups": signups,
            "remaining_places": remaining_places,
            "event_finished": event_finished,
        }
        return render(request, "events_listing/postevent_detail.html", context)

    def post(self, request, slug):
        """
        Handle POST requests for signing up, unregistering, and commenting on a post event.
        """
        post = get_object_or_404(PostEvent, slug=slug, status=1)
        if 'signup' in request.POST:
            if post.signups.count() < post.max_participants:
                EventSignUp.objects.create(event=post, user=request.user)
                messages.success(request, 'You have signed up for the event. You should receive a confirmation email shortly.')
                if request.user.email:
                    send_signup_confirmation_email(request.user, post)
            else:
                messages.error(request, 'The event is full.')
        elif 'unregister' in request.POST:
            EventSignUp.objects.filter(event=post, user=request.user).delete()
            messages.success(request, 'You have unregistered from the event. You should receive a confirmation email shortly.')
            if request.user.email:
                send_unregistration_confirmation_email(request.user, post)
        else:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.success(request, 'Comment submitted and awaiting approval')

        return redirect('postevent_detail', slug=post.slug)

def comment_edit(request, slug, comment_id):
    """
    View to handle editing a comment on a post event.
    """
    if request.method == "POST":
        post = get_object_or_404(PostEvent, slug=slug, status=1)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('postevent_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    post = get_object_or_404(PostEvent, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('postevent_detail', args=[slug]))
