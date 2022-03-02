from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class manager(BaseUserManager):
    use_in_migration = True
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('you must have phone')
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone,password):
        user = self.create_user(phone, password)
        user.is_superuser = True
        # extra.setdefault('is_staff', True)
        # extra.setdefault('is_superuser', True)
        user.save(using=self._db)
        return user

    

#  user model with 'phone' as username
class Userperson(AbstractBaseUser):

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