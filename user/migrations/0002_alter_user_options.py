# Generated by Django 4.2.4 on 2023-09-02 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'клиент рассылки', 'verbose_name_plural': 'клиенты рассылки'},
        ),
    ]
