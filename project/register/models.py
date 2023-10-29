from django.db import models

class Reger(models.Model):
    admin_password = models.CharField('Пароль для доступа в галерею', max_length=50, default='')

    def __str__(self):
        return self.admin_password

    class Meta:
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'