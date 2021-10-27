from django.contrib import admin
from .models import *

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "is_verified"]

admin.site.register(UserModel, UserModelAdmin)

admin.site.register(OTPModel)