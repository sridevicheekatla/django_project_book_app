from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User,bookData
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = [
        [None, {'fields': ['email', 'password']}],

        [('Permissions'), {'fields': ['is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions']}],
    ]
    add_fieldsets = [
        [None, {
            'classes': ['wide',],
            'fields': ['email', 'password1', 'password2'],
        }],
    ]
    list_display = ['email', 'is_staff']
    search_fields = ['email']
    ordering = ['email',]
class bookDataadmin(admin.ModelAdmin):
    list_display=['book_name','author','publication','edition_number']

admin.site.register(bookData,bookDataadmin)
