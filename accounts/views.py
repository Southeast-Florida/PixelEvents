from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.utils.timezone import now

from .forms import UserRegisterForm, OrganizerRegisterForm

def choose_register_view(request):
    return render(request, 'accounts/choose_register.html')  # 👈 добавлено

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/user_register.html', {'form': form})

def organizer_register_view(request):
    if request.method == 'POST':
        form = OrganizerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = OrganizerRegisterForm()
    return render(request, 'accounts/organizer_register.html', {'form': form})

class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        send_mail(
            subject="Login Notification",
            message=f"User {user.email} logged in at {now()}.",
            from_email="admin@example.com",
            recipient_list=[user.email],
            fail_silently=True,
        )
        return super().form_valid(form)
