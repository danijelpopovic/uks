from django.shortcuts import get_object_or_404

from repository.models import Repository
from . import models
from django import forms


class IssueForm(forms.ModelForm):
    class Meta:
        model = models.Issue
        fields = [
            "title",
            "description",
            "workers"
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'rows': 15, 'cols': 100, 'class': "form-control"})
        }
