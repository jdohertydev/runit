from django.urls import path
from . import views

"""
URL patterns for account-related views.
"""

urlpatterns = [
    path('account/update/', views.account_update, name='account_update'),
    path('account/change-password/', views.account_password_change, name='account_password_change'),
    path('account/delete/', views.account_delete, name='account_delete'),
]
