from django.contrib import admin
from front.models import *
# Register your models here.


class OptionAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")
    list_editable = ("value", )


admin.site.register(Option, OptionAdmin)