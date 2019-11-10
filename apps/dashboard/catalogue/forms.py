from django import forms

from oscar.apps.dashboard.catalogue.forms import ProductClassForm as CoreProductClassForm
from oscar.core.loading import get_model


ProductFile = get_model('catalogue', 'ProductFile')


class ProductFileForm(forms.ModelForm):

    class Meta:
        model = ProductFile
        fields = ('file',)
        widgets = {
            'file': forms.FileInput
        }


class ProductClassForm(CoreProductClassForm):
    class Meta(CoreProductClassForm.Meta):
        fields = ['name', 'requires_shipping', 'track_stock', 'options', 'is_digital']
