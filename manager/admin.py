from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Manager
from user_profile.models import Order
from chat.models import Chat

class ManagerAdmin(admin.ModelAdmin):
    list_display=('date_joined','first_name','last_name','email',)
    exclude=('is_staff','user_permissions','is_superuser','last_login','is_active','date_joined','groups')
    list_per_page=10
    
    def save_model(self,request,obj,form,change):
        group=Group.objects.filter(name='Managers')[0]
        super(ManagerAdmin,self).save_model(request,obj,form,change)
        obj.groups.add(group)    

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Manager,ManagerAdmin)
