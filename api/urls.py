from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path("booking/", include("bookingapi.urls")),
    path("email/", include("emailapi.urls")),
    path("auth/", include("users.urls")),
    path('api-auth/', include('rest_framework.urls')),
]