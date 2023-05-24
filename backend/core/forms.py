from django import forms

from backend.core.models import Review


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text"]

