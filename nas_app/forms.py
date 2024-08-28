# ./nas_app/forms.py

from django import forms
from .models import NASFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = NASFile
        fields = ['file', 'description']
