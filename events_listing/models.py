from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class PostEvent(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="event_posts"
    )
    location = models.CharField(max_length=200)
    description = models.TextField()
    max_participants = models.PositiveIntegerField()
    course_map = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)