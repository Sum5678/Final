# Generated by Django 4.2.5 on 2024-01-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0004_remove_book_image_book_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
