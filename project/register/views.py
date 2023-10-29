from django.shortcuts import render, redirect
from .forms import RegerForm
from .forms import Reger

def index(request):
    form = RegerForm()
    error = ''

    data = {
        'form': form,
        'error': error,
    }

    if request.method == 'POST':
        form = RegerForm(request.POST)
        password = form.data.get('admin_password')
        register_entry = Reger.objects.first()
        if register_entry and password == register_entry.admin_password:        
                return redirect('main')

    return render(request, 'main/index.html', data)