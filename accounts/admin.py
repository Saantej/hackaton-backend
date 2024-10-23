from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core import models, constants
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Настройка отображения полей в списке пользователей
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    # Настройка полей для редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'surname', 'phone_number', 'profile_picture', 'birth_date', 'country')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Поля, которые отображаются при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    # Поиск по email и username
    search_fields = ('email', 'username')
    ordering = ('email',)
