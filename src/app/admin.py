from django.contrib import admin

from app.internal.admin_users.presentation.admin import AdminUserAdmin
from app.internal.remembrance.presentation.admin import PlaceAdmin

admin.site.site_title = "Places Remember"
admin.site.site_header = "Places Remember"
