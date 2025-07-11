from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

class Flat(models.Model):
    

    owners = models.ManyToManyField(
        'Owner',
        related_name='owned_flats',
        verbose_name='Собственники',
        blank=True
    )

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    new_building = models.BooleanField(
    'Новостройка',
    null=True,
    blank=True,
    db_index=True, 
    help_text='Отметьте, если квартира в новостройке'
)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', null=True, blank=True, db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    
    likes = models.ManyToManyField(
        User,
        verbose_name='Лайки',
        related_name='liked_flats',
        blank=True,
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь, который жалуется',
        related_name='complaints'
    )
    flat = models.ForeignKey(
        'Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира, на которую жалуются',
        related_name='complaints'
    )
    text = models.TextField('Текст жалобы')
    created_at = models.DateTimeField('Дата создания жалобы', auto_now_add=True)

    def __str__(self):
        return f'Жалоба от {self.user} на квартиру {self.flat}'
    
    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class Owner(models.Model):
    full_name = models.CharField('ФИО владельца', max_length=200)
    pure_phone = PhoneNumberField('Нормализованный телефон', blank=True, null=True, region='RU')
    
    

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Собственник'
        verbose_name_plural = 'Собственники'