# Generated by Django 4.1.7 on 2023-10-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_reger_admin_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reger',
            name='password',
        ),
        migrations.AlterField(
            model_name='reger',
            name='admin_password',
            field=models.CharField(default='', max_length=50, verbose_name='Пароль администратора'),
        ),
    ]