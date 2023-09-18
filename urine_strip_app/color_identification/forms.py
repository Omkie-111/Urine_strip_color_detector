# urine_strip_app/forms.py

from django import forms
from .models import UrineStrip

class UrineStripUploadForm(forms.ModelForm):
    class Meta:
        model = UrineStrip
        fields = ['image']
