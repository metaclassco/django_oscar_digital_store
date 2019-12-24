from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ProductFile


@receiver(pre_save, sender=ProductFile)
def determine_product_file_meta(sender, instance, *args, **kwargs):
    instance.size = instance.file.size
    instance.mimetype = instance.file._file.content_type
    instance.filename = instance.file.name
