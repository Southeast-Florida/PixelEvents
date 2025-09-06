from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.utils.timezone import now
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm, OrganizerRegisterForm

# Выбор типа регистрации
def choose_register_view(request):
    return render(request, 'accounts/choose_register.html')

# Регистрация обычного пользователя с авто-входом, если email уже существует
def user_register_view(request):
    User = get_user_model()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Если пользователь уже существует — пробуем авторизовать
        if User.objects.filter(email=email).exists():
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('participant_dashboard')
            else:
                # Тихо возвращаем форму без вывода ошибок
                return render(request, 'accounts/user_register.html', {'form': form})

        # Если пользователь новый — обычная регистрация
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('participant_dashboard')
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/user_register.html', {'form': form})

# Регистрация организатора с авто-входом, если email уже существует
def organizer_register_view(request):
    User = get_user_model()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('create_event')
            else:
                form = OrganizerRegisterForm()
                form.add_error('email', 'Account already exists. Please log in with correct password.')
                return render(request, 'accounts/organizer_register.html', {'form': form})

        form = OrganizerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_event')
    else:
        form = OrganizerRegisterForm()

    return render(request, 'accounts/organizer_register.html', {'form': form})

# Вход с отправкой уведомления по email
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
