from . import models
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            "title",
            "content"
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'content': forms.Textarea(attrs={'rows': 7, 'cols': 300, 'class': "form-control"})
        }
