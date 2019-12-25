from django.conf import settings
from django.contrib.sites.models import Site
from django.dispatch import receiver

from oscar.apps.order.signals import order_status_changed
from oscar.core.loading import get_class, get_model


CommunicationEventType = get_model('customer', 'CommunicationEventType')
Dispatcher = get_class('customer.utils', 'Dispatcher')

ORDER_PAID_TYPE_CODE = 'ORDER_PAID'


@receiver(order_status_changed)
def send_order_paid_notifications(sender, order, old_status, new_status, **kwargs):
    if new_status == settings.OSCAR_ORDER_PAID_STATUS:
        ctx = {
            'order': order, 'site': Site.objects.get_current()
        }
        messages = CommunicationEventType.objects.get_and_render(code=ORDER_PAID_TYPE_CODE, context=ctx)
        dispatcher = Dispatcher()
        dispatcher.dispatch_order_messages(order, messages, **kwargs)
