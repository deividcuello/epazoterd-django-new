from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


urlpatterns = [
    path("api/", include("api.urls")),
    # path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)