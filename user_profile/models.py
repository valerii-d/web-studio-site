from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.urls import reverse

class Order(models.Model):
    STATUS_CHOICES=(
        ('processing','Processing'),
        ('deviation','Deviation'),
        ('development','Development'),
        ('done','Done')
    )
    user=models.ForeignKey(User,related_name='user_orders',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='processing')
    description=models.TextField()
    deadline=models.DateTimeField(default=timezone.now())
    price=models.IntegerField(null=True,validators=[MinValueValidator(1),])
    paid=models.BooleanField(default=False)

    def __str__(self):
        return  self.created.strftime('%H:%M:%S %d.%m.%Y ')+self.user.email
    class Meta:
        ordering=('-created',)
        verbose_name='Order'
        verbose_name_plural='Orders'

    def get_absolute_url(self):
        return reverse('order',args=[
            self.pk,
        ])
