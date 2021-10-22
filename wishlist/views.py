from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wish, CustomUser
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
        for user in CustomUser.objects.filter(id__exact=wishlist_user_id):
            birthday = datetime.date(year, user.birthday.month, user.birthday.day)
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

        return context

class WishCreateView(CreateView):
    model = Wish
    template_name = 'wish_create.html'
    fields = ['name', 'description', 'image', 'shop_url', 'price', 'user']
