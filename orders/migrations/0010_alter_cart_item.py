# Generated by Django 4.2 on 2023-05-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_rename_customer_cart_customer_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(blank=True, to='orders.cart_object'),
        ),
    ]
