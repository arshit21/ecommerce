# Generated by Django 4.2 on 2023-05-09 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_sales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_6',
        ),
    ]