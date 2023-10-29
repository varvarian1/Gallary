from django.shortcuts import render
from .models import Photo, Category
import os

# Create your views here.

def index(request):
    photo = Photo.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/main.html', {'photo': photo, 'categories': categories})

def delete_image(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл {file_path} успешно удален.")
    else:
        print(f"Файл {file_path} не существует.")

# Пример использования
image_file = "media_cdn/photo.jpg"
delete_image(image_file)