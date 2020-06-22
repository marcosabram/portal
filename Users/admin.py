from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import User 
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('last_name','first_name','tipo')
    list_filter = ()
    ordering = ['last_name','first_name']

    fieldsets = UserAdmin.fieldsets + (
        ('Info extra', {'fields': ('tipo',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Info extra', {'fields': ('tipo',)}),
    )

admin.site.register(User,CustomUserAdmin)
