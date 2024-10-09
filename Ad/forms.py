from django import forms
from django.contrib.auth.forms import AdForm
from typing import Any 
from .models import Ad


class AdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
                field.widget.attrs["class"] = "form-control"
                


    class Meta:
        model = Ad
        fields = ["title", "owner", "description"]            