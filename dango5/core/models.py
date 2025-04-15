from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = RichTextField('Содержание')
    image = models.ImageField('Изображение', upload_to='news/')
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    slug = models.SlugField('URL', max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

class Portfolio(models.Model):
    title = models.CharField('Название', max_length=200)
    description = RichTextField('Описание')
    image = models.ImageField('Изображение', upload_to='portfolio/')
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    is_published = models.BooleanField('Опубликовано', default=True)
    slug = models.SlugField('URL', max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['-created_date']

class Page(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = RichTextField('Содержание')
    slug = models.SlugField('URL', max_length=200, unique=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['title']