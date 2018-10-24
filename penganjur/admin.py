from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Aktiviti #import table aktiviti

# Register your models here.
#admin.site.register(Aktiviti) 
@admin.register(Aktiviti)
class AktivitiAdmin(ImportExportModelAdmin):
	pass