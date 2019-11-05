from oscar.apps.dashboard.catalogue import views

from .formsets import ProductFileFormSet


class ProductCreateUpdateView(views.ProductCreateUpdateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formsets['product_file_formset'] = ProductFileFormSet
