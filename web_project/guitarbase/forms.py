from django import forms
from django.forms import ModelForm

from .models import *

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = "__all__"

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        exclude = ['artist']

class VerseForm(forms.ModelForm):

    class Meta:
        model = Verse
        exclude = ['song']

class ChorusForm(forms.ModelForm):

    class Meta:
        model = Chorus
        exclude = ['song']

class BridgeForm(forms.ModelForm):

    class Meta:
        model = Bridge
        exclude = ['song']