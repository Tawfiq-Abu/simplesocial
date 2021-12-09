from django.db import models
from django.contrib import auth
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,username,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True')

        return self.create_user(email,username,password,**other_fields)

    def create_user(self,email,username,password,**other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email= email,username= username,**other_fields)
        user.set_password(password)
        user.save()
        return user

# class User(auth.models.User,auth.models.PermissionsMixin):
#     def __str__(self):
#         return '@{}'.format(self.username)

class UserBase(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email_address'),unique=True)
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150,blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomAccountManager()

    # telling django the username field should be email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    
