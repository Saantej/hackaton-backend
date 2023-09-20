from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api import urls as api_urls
from core import urls as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(core_urls)),
    path('api/', include(api_urls)),

    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
