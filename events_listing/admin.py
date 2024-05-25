from django.contrib import admin
from .models import PostEvent, Comment, EventSignUp
from django_summernote.admin import SummernoteModelAdmin

@admin.register(PostEvent)
class EventPostAdmin(SummernoteModelAdmin):
    list_display = ('event_name', 'slug', 'status')
    search_fields = ['event_name', 'description']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('event_name',)}
    summernote_fields = ('description',)

    # Specify the order of fields in the admin form
    fields = ['event_name', 'slug', 'date', 'race_type', 'author', 'location', 'course_map', 'description', 'max_participants', 'status']

@admin.register(EventSignUp)
class EventSignUpAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'signed_up_on')
    list_filter = ('event', 'signed_up_on')
    search_fields = ('event__event_name', 'user__username')

# Register Comment model
admin.site.register(Comment)
