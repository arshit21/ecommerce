# Generated by Django 4.2 on 2023-05-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
