# Generated by Django 4.2.4 on 2023-08-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eightStore', '0004_remove_order_game_remove_order_quantity_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to='static/games'),
        ),
    ]
