from . import models
from django import forms

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = models.Repository
        fields = [
            "name",
            "description",
            "isPrivate",
            "contributions"
        ]
        widgets = {
          'name': forms.TextInput(attrs={'class': "form-control"}),
          'description': forms.Textarea(attrs={'rows': 15, 'cols': 100, 'class': "form-control"})
        }

