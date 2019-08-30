from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('books-api/', include('books_api.urls')),
    path('orders/', include('orders.urls')),
    path('blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
