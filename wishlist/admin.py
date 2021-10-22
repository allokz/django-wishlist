from django.contrib import admin
from wishlist.models import CustomUser, Wish


admin.site.register(CustomUser)

@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'user')