from django.contrib import admin

from . import models


class SingleObjectAdminMixin:
    def has_add_permission(self, request, obj=None):
        # Разрешаем создать только один объект
        settings_count = models.SiteSettings.objects.count()
        return settings_count < 1


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(SingleObjectAdminMixin, admin.ModelAdmin):
    pass


@admin.register(models.CompanyContacts)
class CompanyContactsAdmin(SingleObjectAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(models.TextPage, admin.ModelAdmin)
admin.site.register(models.FeedbackRequest, admin.ModelAdmin)
admin.site.register(models.TelegramBotCredentials, admin.ModelAdmin)
