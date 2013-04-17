from django.db import models
from django import forms
from django.contrib.localflavor.us import models as localflavormodels

import django_filepicker

# Add field introspection for FPFileField 
# See http://south.aeracode.org/wiki/MyFieldsDontWork
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django_filepicker\.models\.FPFileField"])

# Create your models here.
class Evidence(models.Model):
    #FPFileField is a field that will render as a filepicker dragdrop widget, but
    #When accessed will provide a File-like interface (so you can do fpfile.read(), for instance)
    fpfile = django_filepicker.models.FPFileField(upload_to='uploads')
    name = models.CharField(max_length=255)
    phone = localflavormodels.PhoneNumberField(max_length=255)
    email = models.EmailField(max_length=255)

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence