from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(
        verbose_name="Содержимое",
    )
    image = models.ImageField(verbose_name="Изображение", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Признак публикации")
    counted_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"Заголовок - {self.title}, контент = {self.content}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
