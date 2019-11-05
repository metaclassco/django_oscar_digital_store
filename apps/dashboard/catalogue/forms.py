from django import forms

from oscar.core.loading import get_model


ProductFile = get_model('catalogue', 'ProductFile')


class ProductFileForm(forms.ModelForm):

    class Meta:
        model = ProductFile
        fields = ('file',)
        widgets = {
            'file': forms.FileInput
        }
