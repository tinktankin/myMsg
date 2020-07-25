from django import forms
from .models import Social


class Social_form(forms.ModelForm):
    class Meta:
        model= Social
        fields = ['facebook_link','linkedin_link','twitter_link']