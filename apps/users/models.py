from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from apps.users.managers import UserManager

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone number"), region="UZ", unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return tokens

    def __str__(self):
        return "{}".format(self.first_name)
