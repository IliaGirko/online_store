from django.db import models
from users.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", null=True, blank=True, default="Описание отсутствует")
    image = models.ImageField(verbose_name="Фото", null=True, blank=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="category",
        verbose_name="Категория",
        null=True,
        blank=True,
    )
    price = models.PositiveIntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    is_active = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(to=CustomUser,
                              on_delete=models.CASCADE,
                              verbose_name="Владелец публикации",
                              null=True,
                              blank=True,
                              )


    def __str__(self):
        return f"Наименование - {self.name}, стоимость = {self.price}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
