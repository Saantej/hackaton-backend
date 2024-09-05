from django.contrib import admin

from core import models, constants
from . import mixins
from rangefilter.filters import DateRangeFilterBuilder


@admin.register(models.FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    list_filter = (("created_at", DateRangeFilterBuilder()),)


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(mixins.SingleObjectAdminMixin, admin.ModelAdmin):
    pass


@admin.register(models.CompanyContacts)
class CompanyContactsAdmin(mixins.SingleObjectAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(models.TextPage, admin.ModelAdmin)
admin.site.register(models.TelegramBotCredentials, admin.ModelAdmin)
