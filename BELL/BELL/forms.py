from django import forms
from sellitem.models import ListItem


"""class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ('name', 'image')"""


class SellItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ('itemname', 'condition', 'description', 'tag', 'base_price', 'main_image', 'other_images')
