from django.contrib import admin
from rent.models import Rent
from import_export.admin import  ImportExportActionModelAdmin


class RentAdmin(ImportExportActionModelAdmin):
    list_display = ['start_data','end_data']
    search_fields = ['start_data']
    list_filter = ('payment','place','client_id')



admin.site.register(Rent,RentAdmin)