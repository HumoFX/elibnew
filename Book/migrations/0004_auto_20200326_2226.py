# Generated by Django 3.0.4 on 2020-03-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20200326_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_get',
            field=models.DateField(auto_now_add=True, verbose_name='Дата получения'),
        ),
    ]
