from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class MainMenuItem(models.Model):
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return reverse('cafe:home') + f'#{self.slug}'

    def __str__(self):
        return f'{self.title}/{self.slug}'

    class Meta:
        ordering = ('position',)




class Footer(models.Model):
    address = RichTextField()
    reservation = RichTextField()
    opening_hours = RichTextField()
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    copyright_text = RichTextField()
    credits_text = RichTextField()

    def __str__(self):
        return 'Footer Info'
