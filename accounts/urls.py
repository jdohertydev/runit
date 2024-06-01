from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.account_update, name='account_update'),
    path('delete/', views.account_delete, name='account_delete'),
]
