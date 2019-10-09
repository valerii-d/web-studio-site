from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Manager(User):
    bio = models.TextField(max_length=500, null=True,blank=True)
    location = models.CharField(max_length=30, null=True,blank=True)
    
    def save(self,*args,**kwargs):
        self.is_staff=True
        self.password=make_password(self.password)
        super(Manager,self).save(*args,**kwargs)
    
    class Meta:
        db_table='managers'
        ordering=('-username',)
        verbose_name='Manager'
        verbose_name_plural='Managers'
