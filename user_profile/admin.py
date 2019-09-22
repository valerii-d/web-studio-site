from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=('created','status','deadline','price','paid',)
    list_filter=('created','status','deadline','paid',)
    fieldsets=(
        (
            None,
            {
                'fields':(('status','paid'),'price',)
            }
        ), 
    )

admin.site.register(Order,OrderAdmin)
