# Generated by Django 4.1.7 on 2023-10-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_reger_name_reger_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='reger',
            name='admin_password',
            field=models.CharField(default='', max_length=50, verbose_name='Пороль Админа'),
        ),
    ]
