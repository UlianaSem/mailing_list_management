# Generated by Django 4.2.4 on 2023-09-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0006_alter_log_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки'),
        ),
    ]