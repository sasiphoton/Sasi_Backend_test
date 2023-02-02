from django.contrib import admin
from .models import TFUser


class TFUserAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'role', 'active_role']


admin.site.register(TFUser, TFUserAdmin)
