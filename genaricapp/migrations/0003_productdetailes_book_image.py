# Generated by Django 3.2.7 on 2021-09-09 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('genaricapp', '0002_rename_book_cost_productdetailes_book_cost_finall'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetailes',
            name='book_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
