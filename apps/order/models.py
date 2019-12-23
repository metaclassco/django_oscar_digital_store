from django.conf import settings

from oscar.apps.order.abstract_models import AbstractOrder


class Order(AbstractOrder):
    @property
    def is_paid(self):
        return self.status == settings.OSCAR_ORDER_PAID_STATUS


from oscar.apps.order.models import *  # noqa isort:skip
