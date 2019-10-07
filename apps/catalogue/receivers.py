import mimetypes
import os

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ProductFile


@receiver(pre_save, sender=ProductFile)
def determine_product_file_meta(sender, instance, *args, **kwargs):
    instance.size = os.path.getsize(instance.file.path)
    instance.mimetype = mimetypes.guess_type(instance.file.path)[0]
