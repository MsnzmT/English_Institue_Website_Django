from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'full_name',
                'email',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'username',
        'email',
        'full_name',
        'is_staff',
    )

    search_fields = (
        'username',
        'full_name',
        'phone_number',
        'email',
    )
    
    
@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    pass