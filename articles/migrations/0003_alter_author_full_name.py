# Generated by Django 3.2.14 on 2022-07-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220713_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='author full name'),
        ),
    ]