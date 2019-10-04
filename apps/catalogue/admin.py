from django.contrib import admin

from .models import ProductFile


admin.site.register(ProductFile)


from oscar.apps.catalogue.admin import *  # noqa
