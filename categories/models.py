from django.db import models

from django.utils.text import slugify
from core.models import AbstractTimestampFields


class Category(AbstractTimestampFields):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
