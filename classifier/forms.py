from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Classifier


class ClassifierForm(forms.ModelForm):
    class Meta:
        model = Classifier
        fields = ('name', 'category', 'data')
