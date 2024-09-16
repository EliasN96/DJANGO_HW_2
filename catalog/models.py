from django.core.validators import MinValueValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите название')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание')
    photo = models.ImageField(
        upload_to='product/photo',
        verbose_name='Фото',
        help_text='Загрузите изображение продукта',
        **NULLABLE
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=False,
        help_text='Введите цену',
        verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at', 'category']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите название')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Название версии')
    is_version_active = models.BooleanField(default=True, verbose_name='Признак версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.product} - {self.version_number}'
