from django import forms
from django.forms import widgets
from .models import Wish

wishform_widgets = {
    'name': widgets.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Name",
    }),
    'description': widgets.Textarea(attrs={
        'class': "form-control",
        'placeholder': "Beschreibung",
        'style': "height: 100px;",
    }),
    'shop_url': widgets.URLInput(attrs={
        'class': "form-control",
        'placeholder': "Link",
    }),
    'price': widgets.NumberInput(attrs={
        'class': "form-control",
        'placeholder': "Preis",
    }),
    'image': widgets.ClearableFileInput(attrs={
        'class': "form-control",
    }),
}

class WishCreateForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'description', 'image', 'shop_url', 'price', 'user']

