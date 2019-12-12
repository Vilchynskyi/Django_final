from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=55)
    slug = AutoSlugField(
        populate_from=title,
        unique=True,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=70)
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        null=True
    )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    price = models.FloatField()
    discount = models.FloatField(
        verbose_name='скидка',
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0),
        ],
        default=0.0)

    desc = models.TextField(max_length=255)

    in_stock = models.BooleanField()

    pub_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(
        upload_to='book',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:book', kwargs={'slug': self.slug, 'pk': self.pk})

    @property
    def short_desc(self):
        return self.desc[:20] + '...' if len(self.desc) > 20 else self.desc

    @property
    def main_price(self):
        return self.price - self.price * self.discount / 100

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
