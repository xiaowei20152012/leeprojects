from django.contrib import admin

from sunuser.dbmodels import Blog,Author,Entry
from sunuser.models import User,Roles,Permission,ThirdPartyRelation,UserRoles,RolesPermission

# Register your models here.


admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
#admin.site.register(User)
#admin.site.register(Roles)
#amdin.site.register(Permission)
#admin.site.register(ThirdPartyRelation)
#admin.site.register(UserRoles)
#admin.site.register(RolesPermission)



