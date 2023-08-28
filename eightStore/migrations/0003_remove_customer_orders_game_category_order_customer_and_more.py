# Generated by Django 4.2.4 on 2023-08-20 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eightStore', '0002_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='orders',
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(to='eightStore.category'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eightStore.customer'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='game',
        ),
        migrations.AddField(
            model_name='order',
            name='game',
            field=models.ManyToManyField(to='eightStore.game'),
        ),
    ]