from django.conf import settings

from oscar.apps.order.abstract_models import AbstractOrder


class Order(AbstractOrder):
    @property
    def is_paid(self):
        return self.status == settings.OSCAR_ORDER_PAID_STATUS

    def get_lines_with_digital_products(self):
        return self.lines.filter(product__product_class__is_digital=True)

    def has_digital_products(self):
        digital_products = self.get_lines_with_digital_products()
        return digital_products.exists()


from oscar.apps.order.models import *  # noqa isort:skip
