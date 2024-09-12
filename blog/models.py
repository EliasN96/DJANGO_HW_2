from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True, verbose_name="url")
    body = models.TextField(max_length=250, verbose_name='Cодержимое', blank=True, null=True)
    image = models.ImageField(upload_to='blog/photo', verbose_name='Изображение(превью)', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания(записи в БД)')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
