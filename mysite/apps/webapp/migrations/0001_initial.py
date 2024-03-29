# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('education', models.TextField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('linkedIn', models.URLField(blank=True, null=True)),
                ('email', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(max_length=255, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('case', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Disability',
            },
        ),
        migrations.CreateModel(
            name='Litigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Litigations',
            },
        ),
        migrations.CreateModel(
            name='ServicesContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('question', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ServicesContact',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Subscribe',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
