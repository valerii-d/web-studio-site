from django.contrib import admin
from django.contrib.auth.models import User
from .models import Manager
from user_profile.models import Order
from chat.models import Chat

class ManagerAdmin(admin.ModelAdmin):
    list_display=('date_joined','first_name','last_name','email',)
    exclude=('is_staff','user_permissions','is_superuser','last_login','is_active','date_joined')
    list_per_page=10

class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email',)
    exclude=('password','groups','user_permissions','is_superuser')
    list_per_page=10

    def has_add_permission(self,request):
        return False
    
    def has_change_permission(self,request,obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if obj.is_superuser == True:
            users = User.objects.exclude(id=obj.id)
            for user in users:
                chat = Chat()
                chat.save()
                chat.users.add(request.user,user)
        super(UserAdmin,self).save_model(request,obj,form,change)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Manager,ManagerAdmin)
