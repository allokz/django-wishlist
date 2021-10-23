from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/<uuid:pk>', views.WishListView.as_view() , name='wishlist'),
    path('wish/create', views.WishCreateView.as_view(), name='wish-create'),
    path('wish/<int:pk>', views.wish_detail_view, name='wish-detail'),
]