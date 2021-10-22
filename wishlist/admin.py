from django.contrib import admin
from wishlist.models import CustomUser, Wish


admin.site.register(CustomUser)
admin.site.register(Wish)
