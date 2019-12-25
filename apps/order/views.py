from io import BytesIO
import os
import zipfile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import View

from oscar.core.loading import get_model


Order = get_model('order', 'Order')


class DownloadOrderProductFiles(LoginRequiredMixin, View):
    model = get_model('order', 'Order')

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(self.model, user=self.request.user, number=self.kwargs['order_number'])
        if not order.has_digital_products():
            raise PermissionDenied(_('Order does not have digital products.'))

        if not order.is_paid:
            raise PermissionDenied(_('Order files will be available for download after the order is paid.'))

        f = BytesIO()
        zf = zipfile.ZipFile(f, "w")
        response = FileResponse(f, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=order_%s.zip' % order.number

        for line in order.get_lines_with_digital_products():
            product = line.product
            for product_file in product.files.all():
                path, filename = os.path.split(product_file.file.path)
                os.chdir(path)
                zf.write(filename)
        zf.close()

        return response
