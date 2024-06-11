from .models import Comment, PostEvent
from allauth.account.forms import SignupForm
from django import forms

class CommentForm(forms.ModelForm):
    """
    Form for creating or updating a comment on a post.
    """
    class Meta:
        model = Comment
        fields = ('body',)

class CustomSignupForm(SignupForm):
    """
    Custom signup form extending from allauth's default SignupForm.
    Includes additional fields for first name and last name.
    """

    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)

    def save(self, request):
        """
        Save method overridden to include saving first name and last name.
        """
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class EventFilterForm(forms.Form):
    """
    Form for filtering events based on search query, race type, and location.
    """
    q = forms.CharField(required=False, label='Search')
    race_type = forms.ChoiceField(
        required=False,
        choices=[('', 'All')] + PostEvent.RACE_TYPE_CHOICES,
        label='Race Type'
    )
    location = forms.CharField(required=False, label='Location')
