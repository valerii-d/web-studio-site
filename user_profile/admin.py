from django.contrib import admin
from .models import Order
from django.contrib.admin.models import LogEntry
from .models import Manager
from chat.models import Chat
from django.db.models import Q

LogEntry.object_repr
class OrderAdmin(admin.ModelAdmin):
    list_display=('created','status','deadline','price','paid','manager',)
    list_filter=('created','status','deadline','paid','manager',)
    readonly_fields=('description',)
    
    search_fields=['user__email',]

    def get_queryset(self,request):
        orders=super(OrderAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return orders
        return orders.filter(Q(manager=None) | Q(manager=request.user))

    def has_delete_permission(self,request,obj=None):
        return False

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        if obj!=None and request.user.is_superuser:
            self.fieldsets=((None,{'fields':('description','file',)}),)
            self.readonly_fields=('description','status','price','paid','file',)
            return False
        else:
            self.fieldsets=((None,{'fields':('status',('price','paid'),'file',)}),
            ('Details',{'fields':('description',)}))
            self.readonly_fields=('description',)
        return True
    

    def save_model(self,request, obj, form, change):
        obj.manager = request.user.manager
        chat = Chat() #create chat with user and manager
        chat.save()
        chat.users.add(obj.user, obj.manager)
        super(OrderAdmin,self).save_model(request,obj,form,change)
    

admin.site.register(Order,OrderAdmin)
admin.site.site_header="Administration"