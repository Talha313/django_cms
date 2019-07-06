from django.contrib import admin

# Register your models here.
from blogs.models import Tag, Blog, Comment

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
