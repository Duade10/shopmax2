from django.db import models
from core.models import AbstractTimestampFields
from categories.models import Category
from django.contrib.auth.models import User


class Post(AbstractTimestampFields):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="blog/photos")
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
