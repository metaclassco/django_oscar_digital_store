from django.contrib import admin
from django.db import models
from django.forms.widgets import FileInput

from .models import ProductFile


class ProductFileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.FileField: {'widget': FileInput},
    }


admin.site.register(ProductFile, ProductFileAdmin)


from oscar.apps.catalogue.admin import *  # noqa
