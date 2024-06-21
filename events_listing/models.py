from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class PostEvent(models.Model):
    """
    Model representing a post for an event.
    """

    ROAD = "Road"
    TRAIL = "Trail"
    MIXED = "Mixed"

    RACE_TYPE_CHOICES = [
        (ROAD, ROAD),
        (TRAIL, TRAIL),
        (MIXED, MIXED),
    ]

    event_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField()
    race_type = models.CharField(max_length=10, choices=RACE_TYPE_CHOICES)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    location = models.CharField(max_length=200)
    description = models.TextField()
    max_participants = models.PositiveIntegerField()
    course_map = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.event_name} | Posted by {self.author} | Event date {self.date.strftime('%d %B %Y')}"


class Comment(models.Model):
    """
    Model representing a comment on a post event.
    """

    post = models.ForeignKey(
        PostEvent, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment '{self.body}' by {self.author}"


class EventSignUp(models.Model):
    """
    Model representing a user sign-up for an event.
    """

    event = models.ForeignKey(
        PostEvent, on_delete=models.CASCADE, related_name="signups"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_signups"
    )
    signed_up_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("event", "user")

    def __str__(self):
        return f"{self.user.username} signed up for {self.event.event_name}"
