from . import models
from django import forms

class IssueForm(forms.ModelForm):
    class Meta:
        model = models.Issue
        fields = [
            "title",
            "description",
        ]
        widgets = {
          'title': forms.TextInput(attrs={'class': "form-control"}),
          'description': forms.Textarea(attrs={'rows': 50, 'cols': 100, 'class': "form-control"})
        }


