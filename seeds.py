from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.hashers import make_password
from django.db.models import Q

new_admin=User()
new_admin.username='admin'
new_admin.first_name='Ivan'
new_admin.last_name='Ivanov'
new_admin.password=make_password('admin')
new_admin.email='ivanov@gmail.com'
new_admin.is_superuser=True
new_admin.is_staff=True
new_admin.save()
new_group=Group(name='Managers')# new group
new_group.save()
order_permissions=Permission.objects.filter(Q(codename='change_order')|Q(codename='view_order')).all()
new_group.permissions.set(order_permissions)
