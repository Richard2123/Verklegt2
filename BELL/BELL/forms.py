from user.models import Profile
from django_countries.widgets import CountrySelectWidget

from django.forms import ModelForm, widgets
from django import forms
from sellitem.models import ListItem
from user.models import Profile
from checkout.models import Purchase
from django_countries.widgets import CountrySelectWidget


class SellItemForm(ModelForm):

    main_image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'forms-control' }))
    image2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'forms-control'}))
    image3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'forms-control'}))
    image4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'forms-control'}))
    image5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'forms-control'}))

    class Meta:
        model = ListItem
        exclude = [ 'id', 'poster', 'itemurl' ]
        widgets = {
            'itemname': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'base_price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': widgets.Textarea(attrs={'class': 'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
        }


class CheckoutForm(ModelForm):
    class Meta:
        model = Purchase
        exclude = ['id', 'user', 'item']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'first-name'}),
            'last_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'last-name'}),
            'street_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'street-name'}),
            'house_number': widgets.TextInput(attrs={'class': 'contact', 'id': 'house-number'}),
            'city': widgets.TextInput(attrs={'class': 'contact', 'id': 'city'}),
            'country': CountrySelectWidget(attrs={'class': 'contact', 'id': 'country'}),
            'postal_code': widgets.TextInput(attrs={'class': 'contact', 'id': 'postal-code'}),
            'payment_first_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'payment-first-name'}),
            'payment_last_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'payment-last-name'}),
            'card_number': widgets.TextInput(attrs={'class': 'payment', 'id': 'card-number'}),
            'card_expiration': widgets.TextInput(attrs={'class': 'payment', 'id': 'card-expiration'}),
            'card_cvc': widgets.TextInput(attrs={'class': 'from-control', 'id': 'card-cvc'}),
        }
