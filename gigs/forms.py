from django import forms
from django.forms import inlineformset_factory
from .models import Gig, GigSize


class GigForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = [
            "title",
            "category",
            "state",
            "price",
            "description",
            "tags",
            "image",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "field"}),
            "category": forms.Select(attrs={"class": "field select-field"}),
            "state": forms.TextInput(attrs={"class": "field"}),
            "price": forms.NumberInput(attrs={"class": "field"}),
            "description": forms.Textarea(attrs={"class": "field"}),
            "tags": forms.TextInput(attrs={"class": "field"}),
            "image": forms.ClearableFileInput(attrs={"class": "field"}),
        }


GigSizeFormSet = inlineformset_factory(
    Gig,
    GigSize,
    fields=("size", "quantity"),
    extra=1,
    can_delete=True,
    widgets={
        "size": forms.Select(attrs={"class": "field select-field"}),
        "quantity": forms.NumberInput(attrs={"class": "field"}),
    }
)
