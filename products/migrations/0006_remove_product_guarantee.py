# Generated by Django 4.2 on 2023-04-24 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_brand_alter_product_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='guarantee',
        ),
    ]
