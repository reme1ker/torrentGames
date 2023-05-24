from django import forms

from core.models import Review


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text"]

