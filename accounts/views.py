# accounts/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')  # или куда тебе нужно
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

