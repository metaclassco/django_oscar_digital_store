from django.utils.translation import gettext_lazy as _

from oscar.apps.partner.availability import Unavailable
from oscar.apps.partner.strategy import Default as CoreDefault


class DigitalProductUnavailable(Unavailable):
    message = _('Digital assets are not available.')


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        return Default(request)


class Default(CoreDefault):
    def availability_policy(self, product, stockrecord):
        if product.product_class.is_downloadable and product.files.count() == 0:
            return DigitalProductUnavailable()

        return super().availability_policy(product, stockrecord)
