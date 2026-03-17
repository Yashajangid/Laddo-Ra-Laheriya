from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import SellerProfile
@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "display_name", "phone", "city", "state")
@admin.register(User)
class Admin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Contact', {'fields': ('role','phone','city','state','bio')}),
    )
    list_display = ('username','email','role','city','state')
