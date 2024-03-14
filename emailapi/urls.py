from django.urls import path, include
from .views import (
    EmailAPI,
)

urlpatterns = [
    path('send/', EmailAPI.as_view()),
]