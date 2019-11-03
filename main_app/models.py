from django.db import models
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ('KE', 'Kadın Elbisesi'),
    ('EE', 'Erkek Elbisesi')
)

LABEL_CHOICES = (
    ('Y', 'Yeni'),
    ('I', 'İndirimli')
)
CURRENCY_CHOICES = (
    ('D', '$'),
    ('T', 'TL')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    discount_price = models.FloatField(blank= True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices = LABEL_CHOICES, max_length=1)
    currency = models.CharField(choices = CURRENCY_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main_app:product", kwargs={
            'slug': self.slug
        })
