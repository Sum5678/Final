# Generated by Django 4.2.5 on 2024-01-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0002_remove_book_book_id_alter_book_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', '可借阅'), ('checked_out', '借閱中'), ('reserved', '已预约')], default='available', max_length=20),
        ),
    ]