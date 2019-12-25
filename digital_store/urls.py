from django.apps import apps
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('orders/', include(apps.get_app_config('order').urls[0]))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
