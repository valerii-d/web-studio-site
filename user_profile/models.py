from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.core.validators import ValidationError

class Order(models.Model):
    STATUS_CHOICES=(
        ('processing','Processing'),
        ('deviation','Deviation'),
        ('development','Development'),
        ('done','Done')
    )
    id_order=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    status=models.CharField(max_length=11, choices=STATUS_CHOICES,default='processing')
    description=models.TextField()
    deadline=models.DateTimeField()
    price=models.IntegerField(null=True,validators=[MinValueValidator(1),])
    paid=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if self.deadline<=timezone.now():
            raise ValidationError("The date cannot be in the past!")
        super(Order,self).save(*args, **kwargs)

    def __str__(self):
        return  self.created.strftime('%H:%M:%S %d.%m.%Y ')+self.user.email
    class Meta:
        db_table='orders'
        ordering=('-created',)
        verbose_name='Order'
        verbose_name_plural='Orders'

    def get_absolute_url(self):
        return reverse('order',args=[
            self.pk,
        ])
