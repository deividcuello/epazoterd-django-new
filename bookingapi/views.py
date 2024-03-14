from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.response import Response
from rest_framework import status

class BookingApiView(APIView):
    
    # page_size = 5

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        booking = Booking.objects.all().order_by('-created_at')
        # results = self.paginate_queryset(booking, request, view=self)
        serializer = BookingSerializer(booking, many=True)
        bookingCount = booking.count()
        return Response({
            'booking': serializer.data,
            'count': bookingCount}, status=status.HTTP_200_OK)

     # 2. Create
    def post(self, request, *args, **kwargs):
 
        data = { 
            'phone': request.data.get('phone'), 
            'date': request.data.get('date'), 
            'time': request.data.get('time'), 
            'time2': request.data.get('time2'), 
            'email': request.data.get('email'), 
            'booking_code': request.data.get('booking_code'), 
            'additional_info': request.data.get('additional_info'), 
            'people_no': request.data.get('people_no'), 
            'user': request.user.id
            }

        if(not request.data.get('additional_info')):
            data = { 
            'phone': request.data.get('phone'), 
            'date': request.data.get('date'), 
            'time': request.data.get('time'), 
            'time2': request.data.get('time2'), 
            'email': request.data.get('email'), 
            'booking_code': request.data.get('booking_code'), 
            'people_no': request.data.get('people_no'), 
            'user': request.user.id
            }

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            booking_id = list(Booking.objects.all().values_list('id', flat=True))[-1]
  
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, booking_id, user_id):

        try:
            return Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, booking_id, *args, **kwargs):
 
        booking_instance = self.get_object(booking_id, request.user.id)
        if not booking_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookingSerializer(booking_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Delete
    def delete(self, request, booking_id, *args, **kwargs):

        booking_instance = self.get_object(booking_id, request.user.id)
        if not booking_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # get_user = AppUser.objects.all().filter(id=request.user.id)[0]

        booking_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
