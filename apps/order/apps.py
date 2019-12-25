from django.conf.urls import url

import oscar.apps.order.apps as apps
from oscar.core.loading import get_class


class OrderConfig(apps.OrderConfig):
    name = 'apps.order'

    def ready(self):
        super().ready()
        self.download_order_product_files = get_class('order.views', 'DownloadOrderProductFiles')

    def get_urls(self):
        urls = [
            url(r'(?P<order_number>[\w-]*)/download/', self.download_order_product_files.as_view(),
                name='download_order_files'),
        ]
        return super().get_urls() + self.post_process_urls(urls)
