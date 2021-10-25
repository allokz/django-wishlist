from django import forms
from django.forms import widgets
from .models import CustomUser, Wish

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
            'class': "form-control d-none",
            'value': self.request.user.id,
            'readonly': True,
        })

    class Meta:
        model = Wish
        fields = ['name', 'description', 'image', 'shop_url', 'price', 'user']
        widgets = wishform_widgets


class OwnWishCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that the correct id from the current user is assigned to gifter. """
        self.request = kwargs.pop('request')
        self.owner_id = kwargs.pop('owner_id')
        super(OwnWishCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = widgets.TextInput(attrs={
            'class': "form-control d-none",
            'value': self.owner_id,
            'readonly': True,
        })
        self.fields['gifter'].widget = widgets.TextInput(attrs={
            'class': "form-control d-none",
            'value': self.request.user.id,
            'readonly': True,
        })
        self.fields['visibility_to_owner'].widget = widgets.CheckboxInput(attrs={
            'class': "form-check-input d-none",
        })
        self.initial['visibility_to_owner'] = False

    class Meta:
        model = Wish
        fields = ['name', 'description', 'image', 'shop_url', 'price', 'visibility_to_owner', 'user', 'gifter']
        widgets = wishform_widgets


class WishUpdateForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'description', 'image', 'shop_url', 'price']
        widgets = wishform_widgets


class WishReserveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that the correct id for the current user is assigned. """
        self.request = kwargs.pop('request')
        super(WishReserveForm, self).__init__(*args, **kwargs)
        self.fields['gifter'].widget = widgets.TextInput(attrs={
            'class': "form-control d-none",
            'value': self.request.user.id,
            'readonly': True,
        })

    class Meta:
        model = Wish
        fields = ['name', 'description', 'price', 'user', 'gifter']
        widgets = {
            'name': widgets.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Name",
                'readonly': True,
            }),
            'description': widgets.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Beschreibung",
                'style': "height: 100px;",
                'readonly': True,
            }),
            'price': widgets.NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Preis",
                'readonly': True,
            }),
            'user': widgets.TextInput(attrs={
                'class': "d-none",
                'readonly': True,
            }),
        }


class WishCancelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WishCancelForm, self).__init__(*args, **kwargs)
        self.initial['gifter'] = None

    class Meta:
        model = Wish
        fields = ['name', 'description', 'price', 'user', 'gifter']
        widgets = {
            'name': widgets.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Name",
                'readonly': True,
            }),
            'description': widgets.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Beschreibung",
                'style': "height: 100px;",
                'readonly': True,
            }),
            'price': widgets.NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Preis",
                'readonly': True,
            }),
            'user': widgets.TextInput(attrs={
                'class': "d-none",
                'readonly': True,
            }),
            'gifter': widgets.TextInput(attrs={
                'class': "d-none",
                'readonly': True,
            }),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birthday', 'image']
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Vorname",
            }),
            'last_name': widgets.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Nachname",
            }),
            'birthday': widgets.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Geburtstag",
            }),
            'image': widgets.ClearableFileInput(attrs={
                'class': "form-control",
            }),
        }

