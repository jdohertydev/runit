from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class PostEvent(models.Model):
    ROAD = 'Road'
    TRAIL = 'Trail'
    MIXED = 'Mixed'

    RACE_TYPE_CHOICES = [
        (ROAD, 'Road'),
        (TRAIL, 'Trail'),
        (MIXED, 'Mixed'),
    ]

    event_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField()
    race_type = models.CharField(max_length=10, choices=RACE_TYPE_CHOICES)    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )
    location = models.CharField(max_length=200)
    description = models.TextField()
    max_participants = models.PositiveIntegerField()
    course_map = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

class Comment(models.Model):
    post = models.ForeignKey(
        PostEvent, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)    