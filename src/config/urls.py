from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import include, path

from app.internal.app import urls

app_name = "app"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include(urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
