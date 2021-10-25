from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from wishlist.models import CustomUser, Wish


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'id')
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'id')
        }),
        ('Persönliche Informationen', {
            'fields': ('first_name', 'last_name', 'email', 'birthday', 'image')
        }),
        ('Berechtigungen', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Wichtige Daten', {
            'fields': ('last_login', 'date_joined')
        }),
    )

@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'user')