from django.forms import ModelForm
from .models import *
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]