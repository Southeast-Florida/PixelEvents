from django.urls import path
from .views import (
    choose_register_view,  # 👈 добавили
    user_register_view,
    organizer_register_view,
    CustomLoginView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 👇 Новая точка входа — выбор типа регистрации
    path('register/choose/', choose_register_view, name='choose_register'),

    # Раздельная регистрация
    path('register/user/', user_register_view, name='user_register'),
    path('register/organizer/', organizer_register_view, name='organizer_register'),

    # Вход и выход
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Восстановление пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
