from django.contrib import admin
from .models import PostEvent, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(PostEvent)
class EventPostAdmin(SummernoteModelAdmin):

    list_display = ('event_name', 'slug', 'status')
    search_fields = ['event_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('event_name',)}
    summernote_fields = ('description',)
    
# Register your models here.

admin.site.register(Comment)