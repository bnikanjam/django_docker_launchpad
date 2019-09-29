import os

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# Secret admin url if provided otherwise django's default
ADMIN_URL = os.getenv('ADMIN_URL', 'admin')
if not ADMIN_URL.endswith('/'):
    ADMIN_URL += '/'

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),  # the 'api-auth/' route could be anything else

    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),

    path(ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
