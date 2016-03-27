from . import models
from django import forms

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = models.Repository
        fields = [
            "name",
            "description",
            "isPrivate",
        ]

