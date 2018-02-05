from django.contrib import admin
from .models import Document_Template, Printer
# Register your models here.

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'ip_address', 'port', 'mac_address', 'building', 'enabled')

admin.site.register(Printer,PrinterAdmin)

def copy_doc_type(modeladmin, request, queryset):
    import copy

    for doc_type in queryset:
    	# multiple could be selected
    	
        new_doc_type = copy.copy(doc_type) # django copy object
        new_doc_type.id = None   # set 'id' to None to create new object

        new_doc_type.save()    # initial save

class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    actions = [copy_doc_type]

admin.site.register(Document_Template,DocumentTemplateAdmin)