from django.conf import settings
from django.db import models

from oscar.apps.order.abstract_models import AbstractOrder


class Order(AbstractOrder):
    @property
    def is_paid(self):
        return self.status == settings.OSCAR_ORDER_PAID_STATUS

    def get_lines_with_digital_products(self):
        return self.lines.filter(product__product_class__is_downloadable=True)

    def has_digital_products(self):
        digital_products = self.get_lines_with_digital_products()
        return digital_products.exists()


class DownloadAttempt(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


from oscar.apps.order.models import *  # noqa isort:skip
