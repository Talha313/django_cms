# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190716_1943'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Disability',
        ),
        migrations.RemoveField(
            model_name='flsaclaim',
            name='content',
        ),
        migrations.AlterField(
            model_name='about',
            name='biography',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='education',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='FlsaClaim',
        ),
    ]
