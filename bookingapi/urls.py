from django.urls import path, include
from .views import (
    BookingApiView,
    BookingDetailApiView
)

urlpatterns = [
    path('', BookingApiView.as_view()),
    path('<int:booking_id>/', BookingDetailApiView.as_view()),
]