from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from wishlist.models import CustomUser, Wish


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'id', )

@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'user')