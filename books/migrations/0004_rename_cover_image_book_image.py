# Generated by Django 5.2.1 on 2025-05-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_cover_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cover_image',
            new_name='image',
        ),
    ]
