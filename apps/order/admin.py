from django.contrib import admin
from .models import DownloadAttempt

admin.site.register(DownloadAttempt)


from oscar.apps.order.admin import *  # noqa
