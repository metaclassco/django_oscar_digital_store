from django.forms.models import inlineformset_factory

from oscar.core.loading import get_model

from .forms import ProductFileForm


Product = get_model('catalogue', 'Product')
ProductFile = get_model('catalogue', 'ProductFile')


BaseProductFileFormSet = inlineformset_factory(Product, ProductFile, form=ProductFileForm, extra=1)


class ProductFileFormSet(BaseProductFileFormSet):

    def __init__(self, product_class, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
