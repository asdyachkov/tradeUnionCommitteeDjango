import django
from django.db import models


class News(models.Model):

    theme = models.CharField(null=False, max_length=200, verbose_name="Тема новости")
    body = models.TextField(null=False, verbose_name="Текст новости")
    created_at = models.DateTimeField(
        null=False,
        default=django.utils.timezone.now,
        verbose_name="Время создания новости",
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        db_table = "news"
        ordering = ["id", "created_at"]

    def __str__(self):
        return str(self.theme)


class Pins(models.Model):

    theme = models.CharField(null=False, max_length=200, verbose_name="Тема пина")
    description = models.TextField(null=False, verbose_name="Описание пина")
    image_link = models.TextField(null=False, verbose_name="Ссылка на изображение пина")

    class Meta:
        verbose_name = "Пин"
        verbose_name_plural = "Пины"
        db_table = "pins"
        ordering = ["id", "theme"]

    def __str__(self):
        return str(self.theme)


class Documents(models.Model):

    theme = models.CharField(null=False, max_length=200, verbose_name="Тема документа")
    description = models.TextField(null=False, verbose_name="Описание документа")
    admin_upload = models.FileField(upload_to='media', null=False, verbose_name="Файл документа")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        db_table = "documents"
        ordering = ["id", "theme"]

    def __str__(self):
        return str(self.theme)


class Benefits(models.Model):

    theme = models.CharField(null=False, max_length=200, verbose_name="Тема льготы")
    description = models.CharField(null=False, max_length=200, verbose_name="Описание льготы")
    body = models.TextField(null=False, verbose_name="Текст льготы")

    class Meta:
        verbose_name = "Льгота"
        verbose_name_plural = "Льготы"
        db_table = "benefits"
        ordering = ["id", "theme"]

    def __str__(self):
        return str(self.theme)
