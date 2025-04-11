from django import forms
from .models import Receipt, Item, Participant

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["title", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
            }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": "0"})
            }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}
