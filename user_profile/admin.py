from django.contrib import admin
from .models import Order
from django.contrib.admin.models import LogEntry
from .models import Manager

LogEntry.object_repr
class OrderAdmin(admin.ModelAdmin):
    list_display=('created','status','deadline','price','paid',)
    list_filter=('created','status','deadline','paid',)
    fieldsets=(
        (
            None,
            {
                'fields':(('status','paid'),'price','file',)
            }
        ), 
    )
    
    search_fields=['user.first name',]

    def has_delete_permission(self,request,obj=None):
        return False

    def has_add_permission(self,request):
        return False

admin.site.register(Order,OrderAdmin)
admin.site.site_header="Administration"