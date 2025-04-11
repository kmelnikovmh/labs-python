from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auf_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls", namespace='homepage')),
    path("checks/", include("checks.urls", namespace='checks')),

    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", auf_views.LoginView.as_view(), name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
