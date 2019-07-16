from django.db import models
from autoslug import AutoSlugField
from cms.models.fields import Placeholder, PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class About(BaseModel):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True)
    education = HTMLField(null=True, blank=True)
    biography = HTMLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Abouts"


class Contact(BaseModel):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    case = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = "Contact"

class ServicesContact(BaseModel):

    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    question = models.TextField()

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = "ServicesContact"


class Litigation(BaseModel):
    title = models.CharField(max_length=255)
    description = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Litigations"


class Testimonial(BaseModel):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    content =  HTMLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Testimonials"


class Client(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    image = models.ImageField(max_length=255)

    class Meta:
        verbose_name_plural = "Clients"


class Subscribe(BaseModel):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Subscribe"

