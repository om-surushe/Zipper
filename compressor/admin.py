from django.contrib import admin
from compressor.models import Data
# Register your models here.

class DataModelAdmin(admin.ModelAdmin):
    model = Data
    list_display = [
        'id',
        'encoded_string'
        ]


admin.site.register(Data, DataModelAdmin)
