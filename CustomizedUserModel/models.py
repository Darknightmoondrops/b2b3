from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class manager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(phone, password, **extra_fields)
        return user

    

#  user model with 'phone' as username
class Userperson(AbstractUser):

    gender_choice = [
        ('M', 'male'),
        ('F', "female")
    ]
    roles = [
        ('seller', 'Seller'),
        ('shopper', 'Shopper'), 
        ('serviceman', 'Serviceman')
    ]
    username = None
    fullname = models.CharField(max_length=100, verbose_name="Full Name")
    phone = models.CharField(max_length=20,verbose_name="Phone", unique=True)
    image = models.ImageField(upload_to="userphoto/fullname", blank=True, null=True, verbose_name="User Photo")
    address = models.TextField(null=True,blank=True,verbose_name='Address')
    phone_auth = models.BooleanField(default=False,verbose_name='Phone Auth')
    gender = models.CharField(choices=gender_choice, blank=False, null=False, max_length=50,verbose_name='Gender')
    role = models.CharField(choices=roles, max_length=50,verbose_name='Rols')
    is_superuser = models.BooleanField(default=False,blank=True,null=True,verbose_name='Is Super User')
    objects = manager()
    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = []

    def is_staff(self):
        return self.is_superuser
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser