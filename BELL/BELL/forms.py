from django import forms
from sellitem.models import ListItem
from edituserprofile.models import EditProfile


class SellItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ('itemname', 'condition', 'description', 'base_price', 'main_image', 'image2', 'image3', 'image4', 'image5')


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = EditProfile
        fields = ('full_name', 'email', 'country', 'bio', 'profile_image')
