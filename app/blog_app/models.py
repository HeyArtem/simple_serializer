from django.db import models

# простая модель
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано')
    )
    title =models.CharField(verbose_name='Заголовок', max_length=100)
    # img = models.ImageField(verbose_name='Фото новости', upload_to='blog_app/%Y/%m/%d')
    description = models.CharField(verbose_name='Краткое описание', max_length=100, unique=True, blank=True)
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=15)
    
    # класс для кастомизации админки
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
     
    # магичесский метод, что бы выводились имена моделей
    def __str__(self) -> str:
        return self.title
