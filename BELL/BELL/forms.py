from django import forms
from sellitem.models import ItemImage


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ('name', 'image')
