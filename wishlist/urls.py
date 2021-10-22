from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/<uuid:pk>', views.WishListView.as_view() , name='wishlist'),
]