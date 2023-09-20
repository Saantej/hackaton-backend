from django.db import models


class SiteSettings(models.Model):

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    robots = models.TextField("robots.txt", blank=True)
    favicon = models.ImageField("Favicon", upload_to="favicon", blank=True)
    extra_head_html = models.TextField(blank=True)
    extra_body_html = models.TextField(blank=True)

    @classmethod
    def get(cls):
        if not hasattr(cls, "_cached_obj"):
            cls._cached_obj = cls.objects.get()
        return cls._cached_obj

    def __str__(self):
        return "Настройки сайта"


class CompanyContacts(models.Model):

    email = models.EmailField(verbose_name="E-mail", blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=16, blank=True)
    requisites = models.TextField(verbose_name="Реквизиты", blank=True)

    address = models.CharField(verbose_name="Адрес", max_length=128, blank=True)
    address_html_code = models.TextField(verbose_name="HTML код для вставки карты", blank=True)

    class Meta:
        verbose_name = "Контакты компании"
        verbose_name_plural = "Контакты компании"

    def __str__(self):
        return "Контакты компании"


class ExtraFields(models.Model):

    class Meta:
        verbose_name = "Дополнительное поле"
        verbose_name_plural = "Дополнительные поля"

    key = models.CharField(verbose_name="Ключ", help_text="", max_length=20, unique=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100, blank=True)
    text = models.TextField(verbose_name="Текст", blank=True)

    def __str__(self):
        return self.title or self.key


class FeedbackRequest(models.Model):
    email = models.EmailField(verbose_name="E-mail", blank=True)
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия", blank=True)
    phone = models.CharField(max_length=11, verbose_name="Телефон")

    comment = models.TextField(blank=True)

    class Meta:
        verbose_name = "Заявка на обратную связь"
        verbose_name_plural = "Заявки на обратную связь"

    def __str__(self):
        return f'Заявка от {self.phone}'

