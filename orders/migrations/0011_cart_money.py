# Generated by Django 4.2 on 2023-05-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_cart_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]
