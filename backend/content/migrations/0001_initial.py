# Generated by Django 5.2.1 on 2025-05-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
