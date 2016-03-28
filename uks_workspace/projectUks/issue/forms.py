from . import models
from django import forms

class IssueForm(forms.ModelForm):
    class Meta:
        model = models.Issue
        fields = [
            "title",
            "description",
        ]

