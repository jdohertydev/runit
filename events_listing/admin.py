from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import PostEvent, Comment, EventSignUp
from django_summernote.admin import SummernoteModelAdmin

# Define the custom admin action
def export_participants(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="participants.csv"'

    writer = csv.writer(response)
    writer.writerow(['Event Name', 'Event Date', 'Participant Number', 'First Name', 'Last Name', 'Signup Date'])

    for event in queryset:
        signups = EventSignUp.objects.filter(event=event).order_by('signed_up_on')
        for index, signup in enumerate(signups, start=1):
            writer.writerow([
                event.event_name, 
                event.date.strftime('%d %B %Y %H:%M'), 
                index, 
                signup.user.first_name, 
                signup.user.last_name,
                signup.signed_up_on.strftime('%d %B %Y %H:%M')
            ])

    return response

export_participants.short_description = "Export participants for selected events"

class EventPostAdmin(SummernoteModelAdmin):
    list_display = ('event_name', 'slug', 'status')
    search_fields = ['event_name', 'description']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('event_name',)}
    summernote_fields = ('description',)
    actions = [export_participants]  # Add the custom action to the admin

    # Specify the order of fields in the admin form
    fields = ['event_name', 'slug', 'date', 'race_type', 'featured_image', 'author', 'location', 'course_map', 'description', 'max_participants', 'status']

    # Ensures that staff status members only see events they created    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(author=request.user)
        return qs.none()

@admin.register(EventSignUp)
class EventSignUpAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'signed_up_on')
    list_filter = ('event', 'signed_up_on')
    search_fields = ('event__event_name', 'user__first_name', 'user__last_name')

# Register models
admin.site.register(PostEvent, EventPostAdmin)
admin.site.register(Comment)