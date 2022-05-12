from django.forms import ModelForm, widgets
from django import forms
from sellitem.models import ListItem
from user.models import Profile
from django_countries.widgets import CountrySelectWidget


class SellItemForm(ModelForm):

    main_image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'forms-control' }))
    image2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'forms-control'}))
    image3 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'forms-control'}))
    image4 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'forms-control'}))
    image5 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'forms-control'}))

    class Meta:
        model = ListItem
        exclude = [ 'id' ]
        widgets = {
            'itemname': widgets.TextInput(attrs={'class': 'form-control' }),
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
