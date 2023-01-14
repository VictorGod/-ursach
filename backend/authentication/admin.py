from django.contrib import admin
from authentication.models import User
from import_export.admin import ImportExportModelAdmin


# Register your models here.


admin.site.register(User)