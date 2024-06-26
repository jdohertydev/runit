"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path(
        "user-accounts/", include("accounts.urls")
    ),  # Renamed to avoid conflict
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("contact/", include("contact.urls")),
    path("", include("events_listing.urls"), name="events-listing-urls"),
]

# Custom error handlers
handler400 = "myproject.views.custom_400_view"
handler403 = "myproject.views.custom_403_view"
handler404 = "myproject.views.custom_404_view"
handler500 = "myproject.views.custom_500_view"
