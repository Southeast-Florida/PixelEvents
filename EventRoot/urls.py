from django.contrib import admin
from django.urls import path, include

# Для работы с медиафайлами
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключение приложения accounts (регистрация, вход и т.д.)
    path('accounts/', include('accounts.urls')),  # ✅ исправлено

    # Подключение приложения events (создание событий)
    path('events/', include('events.urls')),
]

# Раздача медиафайлов (например, обложек событий) в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
