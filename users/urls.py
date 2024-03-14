from django.urls import path
from django.urls import include, re_path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
	path('users', views.UsersView.as_view(), name='users'),
    path('users/<int:username_id>/', views.UserDetailApiView.as_view()),
	path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh')
	
]