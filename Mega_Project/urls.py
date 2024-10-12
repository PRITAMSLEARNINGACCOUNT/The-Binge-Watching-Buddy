from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as Authentication_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Project_App.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
