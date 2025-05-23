# Generated by Django 5.2.1 on 2025-05-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_users_is_staff_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
