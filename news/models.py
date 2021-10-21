from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True, default="new", verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to='news')
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    published = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class CategoryShop(models.Model):

    name = models.CharField(max_length=150, unique=True, default="new")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Shop(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    image = models.ImageField(upload_to='shop', verbose_name='Изображение')
    logo = models.ImageField(upload_to='shop/icon', verbose_name='Логотип')
    description = models.TextField(max_length=500, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    link = models.URLField()
    category = models.ForeignKey(CategoryShop, on_delete=models.CASCADE, related_name='category_shop')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class WareHouse(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название склада')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    recipient = models.CharField(max_length=100, verbose_name='Получатель')
    town = models.CharField(max_length=30, verbose_name='Город')
    state = models.CharField(max_length=30, verbose_name='Штат')
    index_message = 'Index must be entered in the format: XX XX XX'
    index_regex = RegexValidator(
        regex=r'^\d{6}$',
        message=index_message
    )
    postcode = models.CharField(validators=[index_regex], max_length=6, verbose_name='Индекс')
    phone_message = 'Phone number must be entered in the format: 996 999 999 999'
    phone_regex = RegexValidator(
        regex=r'^(996)\d{9}$',
        message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=12, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='news/warehouse', verbose_name='Изображение')