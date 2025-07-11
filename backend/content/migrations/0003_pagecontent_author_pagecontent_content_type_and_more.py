# Generated by Django 5.2.1 on 2025-06-01 13:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_pagecontent_publish_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='content_type',
            field=models.CharField(default='article', max_length=50),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
