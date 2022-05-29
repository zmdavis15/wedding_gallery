from django import forms
from .models import Photo
from bootstrap_modal_forms.forms import BSModalModelForm

class PhotoForm(BSModalModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
