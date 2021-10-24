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

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that the correct id for the current user is assigned. """
        self.request = kwargs.pop('request')
        super(WishCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = widgets.TextInput(attrs={
            'class': "form-control",
            'value': self.request.user.id,
            'readonly': True,
        })

    class Meta:
        model = Wish
        fields = ['name', 'description', 'image', 'shop_url', 'price', 'user']
        widgets = wishform_widgets

class WishUpdateForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'description', 'image', 'shop_url', 'price']
        widgets = wishform_widgets