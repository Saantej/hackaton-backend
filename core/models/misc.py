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
    first_name = models.CharField(max_length=64, verbose_name="Имя", blank=True)
    phone = models.CharField(max_length=24, verbose_name="Телефон", blank=True)
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка на обратную связь"
        verbose_name_plural = "Заявки на обратную связь"

    def __str__(self):
        return f'Заявка от {self.phone}'


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    BACKLOG = 'backlog'
    BLOCKED = 'blocked'
    IN_PROGRESS = 'in_progress'
    READY_TO_TEST = 'ready_to_test'
    DONE = 'done'

    STATUS_CHOICES = [
        (BACKLOG, 'В ожидании'),
        (BLOCKED, 'Заблокирована'),
        (IN_PROGRESS, 'В процессе'),
        (READY_TO_TEST, 'Готова к тесту'),
        (DONE, 'Завершена'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    complexity = models.CharField(max_length=50, default='medium', verbose_name='Сложность')
    priority = models.CharField(max_length=50, default='medium', verbose_name='Приоритет')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=BACKLOG, verbose_name='Статус')
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE, verbose_name='Создатель')
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks', blank=True, verbose_name='Исполнители')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    assigned_by = models.ForeignKey(User, related_name='assigned_tasks_by', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Назначил')

    def __str__(self):
        return self.title