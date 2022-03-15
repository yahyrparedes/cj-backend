from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('api/company/', include("companies.urls")),  # UI Kits Html files
    path('api/postulant/', include("postulant.urls")),  # UI Kits Html files
    path("", include("apps.home.urls"))  # UI Kits Html files
]
