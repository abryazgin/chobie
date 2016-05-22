from django.contrib import admin

from .models import Scope, UserScope, Role

admin.site.register(Scope)
admin.site.register(UserScope)
admin.site.register(Role)
