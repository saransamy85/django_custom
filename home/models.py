from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .manager import UserManager
from django.contrib.auth import get_user_model
# Create your models here.




class CustomUser(AbstractBaseUser):
    username= None
    phone_number=models.CharField(max_length=10,unique=True)
    
    user_bio=models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects=UserManager()

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=['user_bio']

    def __str__(self):
        return self.phone_number
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,phone_number):
        return True


class person(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=110)
    email=models.EmailField(blank=True)
    
    def __str__(self):
        return self.name
 
class addr(models.Model):
    address=models.TextField()
    person_id=models.ForeignKey(person,on_delete=models.CASCADE)

    def __str__(self):
        return self.address