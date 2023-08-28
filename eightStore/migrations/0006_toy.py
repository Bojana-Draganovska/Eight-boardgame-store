# Generated by Django 4.2.4 on 2023-08-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eightStore', '0005_game_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('short_description', models.TextField(max_length=300, null=True)),
                ('age', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('long_description', models.TextField(max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/games')),
            ],
        ),
    ]