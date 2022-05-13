from django.forms import ModelForm, widgets
from django import forms
from sellitem.models import ListItem
from user.models import Profile
from checkout.models import Purchase
from django_countries.widgets import CountrySelectWidget


class SellItemForm(ModelForm):

    main_image = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    image2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    image3 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    image4 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    image5 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ListItem
        exclude = ['id', 'user', 'itemurl', 'sold', 'highest_bid']
        widgets = {
            'itemname': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'startBid': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        items = super().save(commit=False)
        if commit:
            items.save()
        return items


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        exclude = ['id', 'user', 'rating']
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
            'first_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'first-name', 'name': 'first-name'}),
            'last_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'last-name', 'name': 'last-name'}),
            'street_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'street-name', 'name': 'street-name'}),
            'house_number': widgets.TextInput(attrs={'class': 'contact', 'id': 'house-number', 'name': 'house-number'}),
            'city': widgets.TextInput(attrs={'class': 'contact', 'id': 'city', 'name': 'city'}),
            'country': CountrySelectWidget(attrs={'class': 'contact', 'id': 'country', 'name': 'country'}),
            'postal_code': widgets.TextInput(attrs={'class': 'contact', 'id': 'postal-code', 'name': 'postal-code'}),
            'payment_first_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'payment-first-name'}),
            'payment_last_name': widgets.TextInput(attrs={'class': 'contact', 'id': 'payment-last-name'}),
            'card_number': widgets.TextInput(attrs={'class': 'payment', 'id': 'card-number'}),
            'card_expiration': widgets.TextInput(attrs={'class': 'payment', 'id': 'card-expiration'}),
            'card_cvc': widgets.TextInput(attrs={'class': 'from-control', 'id': 'card-cvc'}),
        }
