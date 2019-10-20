from django.contrib import admin
from .models import Order
from django.contrib.admin.models import LogEntry
from .models import Manager
from chat.models import Chat

LogEntry.object_repr
class OrderAdmin(admin.ModelAdmin):
    list_display=('created','description','status','deadline','price','paid','manager',)
    list_filter=('created','status','deadline','paid','manager',)
    fieldsets=(
        (
            None,
            {
                'fields':('status',('price','paid'),'file',)
            }
        ), 
    )
    
    search_fields=['user__email',]

    def has_delete_permission(self,request,obj=None):
        return False

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request,obj=None):
        # if obj!=None and ( obj.manager==None or  obj.manager_id == request.user.id ):                
        #     return True
        return True

    def save_model(self,request, obj, form, change):
        obj.manager = request.user.manager
        chat = Chat() #create chat with user and manager
        chat.save()
        chat.users.add(obj.user, obj.manager)
        super(OrderAdmin,self).save_model(request,obj,form,change)
    

admin.site.register(Order,OrderAdmin)
admin.site.site_header="Administration"