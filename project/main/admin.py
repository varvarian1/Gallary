from django.contrib import admin
from .models import Photo, Category  # Import the Category model as well
from django.utils.safestring import mark_safe
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview', 'category')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="400" height="400" />'.format(obj.image.url))
        return None

    image_preview.short_description = 'Фото'

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category)  # Register the Category model separately