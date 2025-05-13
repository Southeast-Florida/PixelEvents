
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.utils.timezone import now

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})  # ✅ фикс

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
