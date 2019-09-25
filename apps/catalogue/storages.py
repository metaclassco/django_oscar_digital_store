from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible
from django.utils.functional import cached_property


@deconstructible
class DigitalProductStorage(FileSystemStorage):
    """
    Private storage for files, used by digital products.
    Re-used our private storage class from django-oscar-invoices.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._location = settings.DIGITAL_FILES_ROOT

    def _clear_cached_properties(self, setting, **kwargs):
        if setting == 'DIGITAL_PRODUCTS_ROOT':
            self.__dict__.pop('base_location', None)
            self.__dict__.pop('location', None)

        elif setting == 'FILE_UPLOAD_PERMISSIONS':
            self.__dict__.pop('file_permissions_mode', None)

        elif setting == 'FILE_UPLOAD_DIRECTORY_PERMISSIONS':
            self.__dict__.pop('directory_permissions_mode', None)

    @cached_property
    def base_location(self):
        return self._value_or_setting(self._location, settings.DIGITAL_FILES_ROOT)

    def url(self, name):
        raise ValueError("This file is not accessible via a URL.")
