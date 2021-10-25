from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Wish, CustomUser
from .forms import WishCreateForm, WishUpdateForm, WishReserveForm, WishCancelForm
import datetime


def index(request):
    return render(request, 'index.html')

class WishListView(generic.ListView):
    model = Wish
    template_name = 'wishlist.html'

    def get_queryset(self):
        return Wish.objects.filter(user__exact=self.kwargs.get('pk')).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(WishListView, self).get_context_data(**kwargs)
        

        """ Calculate total price of all wishes on this list """

        wishlist_user_id = self.kwargs.get('pk')

        total = 0
        for wish in Wish.objects.filter(user__exact=wishlist_user_id):
            total += wish.price

        context['total'] = total


        """ Calculate next event """

        today = datetime.date.today()
        year = today.year

        christmas_date = datetime.date(year, 12, 24)
        if today > christmas_date:
            christmas_date = datetime.date(year + 1, 12, 24)

        birthday = datetime.date
        wishlist_username = None
        for user in CustomUser.objects.filter(id__exact=wishlist_user_id):
            birthday = datetime.date(year, user.birthday.month, user.birthday.day)
            wishlist_username = user.username
        if today > birthday:
            birthday = datetime.date(year + 1, birthday.month, birthday.day)

        next_event_name = 'next'
        next_event_date = datetime.date
        days_to_next_event = datetime.date
        days_to_birthday = (birthday - today).days
        days_to_christmas = (christmas_date - today).days

        if days_to_birthday < days_to_christmas:
            next_event_name = 'Geburtstag'
            next_event_date = birthday
            days_to_next_event = days_to_birthday
        else:
            next_event_name = 'Weihnachten'
            next_event_date = christmas_date
            days_to_next_event = days_to_christmas
        
        context['next_event_name'] = next_event_name
        context['next_event_date'] = next_event_date
        context['days_to_next_event'] = days_to_next_event
        context['wishlist_user_id'] = wishlist_user_id
        context['wishlist_user_name'] = wishlist_username

        return context

def wish_detail_view(request, pk):
    return render(request, 'index.html')

class WishCreateView(LoginRequiredMixin, CreateView):
    model = Wish
    form_class = WishCreateForm
    template_name = 'wish_create.html'
    success_url = reverse_lazy('wish-operation-success')

    def get_form_kwargs(self):
        """ Passes the request object to the form class. This is necessary to assign the correct user id to newly created wishes. """
        kwargs = super(WishCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class WishUpdateView(LoginRequiredMixin, UpdateView):
    model = Wish
    form_class = WishUpdateForm
    template_name = 'wish_update.html'
    success_url = reverse_lazy('wish-operation-success')  

class WishDeleteView(LoginRequiredMixin, DeleteView):
    model = Wish
    template_name = 'wish_delete.html'
    success_url = reverse_lazy('wish-operation-success')

class WishReserveView(LoginRequiredMixin, UpdateView):
    model = Wish
    form_class = WishReserveForm
    template_name = 'wish_reserve.html'

    def get_form_kwargs(self):
        """ Passes the request object to the form class. This is necessary to assign the correct user id (from gifter) to reserved wish. """
        kwargs = super(WishReserveView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class WishCancelView(LoginRequiredMixin, UpdateView):
    model = Wish
    form_class = WishCancelForm
    template_name = 'wish_cancel.html'
    success_url = reverse_lazy('wish-operation-success')

def wish_operation_success(request):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
        return HttpResponseRedirect(reverse('wishlist', args=[str(user_id)]))
    else:
        return HttpResponseRedirect(reverse_lazy('index'))


def wishlists_shared_with_me(request):
    return render(request, 'wishlists_shared.html')