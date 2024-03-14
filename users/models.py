from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
		user.is_superuser = True
		user.save()
		return user

class AppUser(AbstractBaseUser, PermissionsMixin):
	STATUS = (
       ('NONE', 'Ninguno'),
       ('INTERNAL', 'Interno'),
    )

	email = models.EmailField(max_length=50, unique=True, null=True, default="")
	username = models.CharField(max_length=50, unique=True)
	isDelete = models.BooleanField(default=True)
	adminAccount = models.BooleanField(default=False)
	status = models.CharField(max_length=50, choices=STATUS, blank=False, null=False, default=STATUS[0][0])
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'isDelete', 'admiAcoount', 'status']
	objects = AppUserManager()
	def __str__(self):
		return self.username