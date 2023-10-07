from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Material

def user_form(request):
    # Fetch all materials from the database
    all_materials = Material.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            return redirect('schoolapp1:success')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form, 'all_materials': all_materials})

def success(request):
    return render(request,'success.html')

