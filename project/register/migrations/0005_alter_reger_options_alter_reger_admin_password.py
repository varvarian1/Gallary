# Generated by Django 4.2.6 on 2023-10-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_remove_reger_password_alter_reger_admin_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reger',
            options={'verbose_name': 'Пароль', 'verbose_name_plural': 'Пароли'},
        ),
        migrations.AlterField(
            model_name='reger',
            name='admin_password',
            field=models.CharField(default='', max_length=50, verbose_name='Пароль для доступа в галерею'),
        ),
    ]