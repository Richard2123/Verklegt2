from django import forms
from sellitem.models import ListItem


class SellItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ('itemname', 'condition', 'description', 'base_price', 'main_image', 'image2', 'image3', 'image4', 'image5')
