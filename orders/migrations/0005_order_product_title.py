# Generated by Django 4.2 on 2023-05-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_vendor_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_title',
            field=models.CharField(blank=True),
        ),
    ]
