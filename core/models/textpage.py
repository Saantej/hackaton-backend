from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from .base import BaseMenuItemModel, BaseSEOModel


class TextPage(BaseMenuItemModel, BaseSEOModel):
    """Тектовая страница"""

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    name = models.CharField("Название", max_length=200)
    content = RichTextField(verbose_name="Контент", config_name='default', blank=True)
    is_generic_page = models.BooleanField(
        verbose_name="Является стандартной страницей",
        help_text="Снять галочку, если страница обрабатывается кастомной view",
        blank=True,
        default=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('text_page', kwargs={'page_slug': self.slug})
