from .models import Videos
from django import forms

class VideoForm(forms.ModelForm):

    class Meta:
        model=Videos
        fields=('url',)
        labels={'url':'YouTube Url'}

class SearchForm(forms.Form):
    search_term=forms.CharField(max_length=255,label='Search for Videos')
