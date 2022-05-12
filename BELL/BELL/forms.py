from django.forms import ModelForm, widgets
from django import forms
from sellitem.models import ListItem
from edituserprofile.models import EditProfile



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


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = EditProfile
        fields = ('full_name', 'email', 'country', 'bio', 'profile_image')
