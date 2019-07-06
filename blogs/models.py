from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.conf import settings


# Create your models here.
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255, default='')
    content = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')
    image = models.ImageField(null=True, blank=True)
    banner = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.title


class Comment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
