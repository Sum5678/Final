# Generated by Django 4.2.5 on 2024-01-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0003_authorform_category_book_image_alter_author_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
    ]