from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True, is_special=False)
        for dish in dishes:
            yield dish

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position', )


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField(blank=True)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('cafe:dish', kwargs={'id': self.id, 'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('category', 'position', )
        constraints = [
            models.UniqueConstraint(
                fields=['position', 'category'],
                name='unique_position_per_category'
            )
        ]
        unique_together = ['id', 'slug']


class Event(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField()
    short_desc = models.TextField(max_length=500, blank=True)
    desc = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='events/', blank=True)
    date_time = models.DateTimeField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Events'
        ordering = ('position', )
        unique_together = ['id', 'slug']


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/')
    is_visible = models.BooleanField(default=True)


class ContactInfoItem(models.Model):
    item = models.CharField(max_length=100)
    value = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ('position', )


class BookTable(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()

    phone_regex = RegexValidator(
        regex=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',
        message='Phone number must be entered in the format: +38(0xx)xxxxxxx',
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=200, blank=True)

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone}: {self.date} {self.time}'

    class Meta:
        ordering = ('-date_in', )