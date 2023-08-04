from django.contrib import admin
from .models import *
# Register your models here.


class InlinePreview(admin.TabularInline):
    model = Preview
    extra = 1
    verbose_name = 'Previews of this Course'



@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    inlines = [InlinePreview]