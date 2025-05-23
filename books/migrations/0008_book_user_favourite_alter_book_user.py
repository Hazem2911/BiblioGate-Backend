# Generated by Django 5.2.1 on 2025-05-17 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user_favourite',
            field=models.ManyToManyField(blank=True, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
