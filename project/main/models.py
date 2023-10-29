from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="400" height="400" />'.format(self.image.url))
        return None

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

@receiver(pre_save, sender=Photo)
def update_image_preview(sender, instance, **kwargs):
    try:
        previous_instance = sender.objects.get(id=instance.id)
        if previous_instance.image != instance.image:
            previous_instance.image.delete(save=False)
    except Photo.DoesNotExist:
        pass
