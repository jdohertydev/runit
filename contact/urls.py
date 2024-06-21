from django.urls import path
from .views import contact_view

"""
URL patterns for the contact form.
"""
urlpatterns = [
    path("", contact_view, name="contact"),
]
