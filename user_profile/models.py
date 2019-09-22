from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
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

    class Meta:
        ordering=('-created',)