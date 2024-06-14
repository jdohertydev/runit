from . import views
from django.urls import path

"""
URL patterns for the views in the Django application.
"""

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('events/', views.PostList.as_view(), name='events_list'),
    path('<slug:slug>/', views.PostEventDetailView.as_view(), name='postevent_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]