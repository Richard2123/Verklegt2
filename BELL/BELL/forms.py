from django import forms
from sellitem.models import ListItem
from user.models import Profile


class SellItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ('itemname', 'condition', 'description', 'base_price', 'main_image', 'image2', 'image3', 'image4', 'image5')


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'full_name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'image': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.widgets.Textarea(attrs={'class': 'form-control'})
        }
