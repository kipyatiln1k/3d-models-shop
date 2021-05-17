from django import forms

from mdls.models import Mdl, Tag


class MdlTagSearchFrom(forms.Form):
    """Форма поиска 3D модели по тэгам"""
    
    tags = forms.ModelMultipleChoiceField(
        label='Выберите нужные категории', 
        queryset=Tag.objects.all(), 
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class':'form-control js-example-basic-multiple'
        }))


    class Meta:
        """Meta definition for Routeform."""

        model = Mdl
        fields = '__all__'
    # TODO: Define form fields here
