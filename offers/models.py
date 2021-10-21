from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Parcel(models.Model):

    STATUS = (
        ('InProcess', 'В процессе'),
        ('Completed', 'Обработан1'),
        ('Completed2', 'Обработан2'),
        ('Completed3', 'Обработан3'),
        ('Sort', 'Сортировка'),
        ('In Stock', 'На складе в KG1'),
        ('In Stock2', 'На складе в KG2'),
        ('In Stock3', 'На складе в KG3'),
        ('NotRegistred', 'Не зарегестрирован')
    )

    order = models.ForeignKey(User, on_delete=models.CASCADE, default=True, verbose_name='Клиент')
    treck = models.CharField(max_length=50, null=False, unique=True, default=False, verbose_name='Трек номер')
    recipient = models.CharField(max_length = 100, verbose_name='Получатель')
    parcels_name = models.CharField(null = False, max_length = 100, verbose_name='Название товара')
    category = models.CharField(max_length=100,null=False,default=False, verbose_name='Категория')
    amount = models.PositiveIntegerField(null = True, verbose_name='Количество')
    price = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2, verbose_name='Цена')
    weight = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2, verbose_name='Вес')
    country = models.CharField(max_length=100, verbose_name=u"Страна")
    web_site = models.URLField(max_length=200,null=False, blank=False, verbose_name='Сайт')
    comment = models.TextField(max_length=324,null=True, verbose_name='Комментарий')
    date = models.DateField(blank=False, auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=100,default = 'NotRegistred', choices = STATUS, verbose_name='Статус')

    class Meta:
        ordering = ['-id']