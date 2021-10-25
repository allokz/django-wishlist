from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/<uuid:pk>', views.WishListView.as_view() , name='wishlist'),
    path('wishlist/shared', views.wishlists_shared_with_me, name='wishlists-shared'),
    path('wish/create', views.WishCreateView.as_view(), name='wish-create'),
    path('wish/<int:pk>', views.wish_detail_view, name='wish-detail'),
    path('wish/<int:pk>/update', views.WishUpdateView.as_view(), name='wish-update'),
    path('wish/<int:pk>/reserve', views.WishReserveView.as_view(), name='wish-reserve'),
    path('wish/<int:pk>/cancel', views.WishCancelView.as_view(), name='wish-cancel'),
    path('wish/<int:pk>/delete', views.WishDeleteView.as_view(), name='wish-delete'),
    path('wish/success', views.wish_operation_success, name='wish-operation-success'),
]