from django.contrib import admin
from django.contrib.auth.models import User
from .models import Manager
from user_profile.models import Order


class ManagerAdmin(admin.ModelAdmin):
    exclude=('is_staff','user_permissions','is_superuser','last_login','is_active','date_joined')

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return queryset.filter(manager=request.user)

class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email',)
    exclude=('password','groups','user_permissions','is_superuser')
    list_per_page=10

    def has_add_permission(self,request):
        return False
    
    def has_change_permission(self,request,obj=None):
        return False


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Manager,ManagerAdmin)
