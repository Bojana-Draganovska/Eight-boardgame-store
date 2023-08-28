# Generated by Django 4.2.4 on 2023-08-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eightStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('orders', models.ManyToManyField(to='eightStore.order')),
            ],
        ),
    ]
