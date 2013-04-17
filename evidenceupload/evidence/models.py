from django.db import models
from django import forms

import django_filepicker

# Create your models here.
class Evidence(models.Model):
    #FPFileField is a field that will render as a filepicker dragdrop widget, but
    #When accessed will provide a File-like interface (so you can do fpfile.read(), for instance)
    fpfile = django_filepicker.models.FPFileField(upload_to='uploads')

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence