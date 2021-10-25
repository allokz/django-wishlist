from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls.base import reverse
import uuid



class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField('Profilbild', upload_to='images/profile/', blank=True, null=True)


class Wish(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)
    description = models.TextField('Beschreibung', max_length=90, blank=True)
    image = models.ImageField('Bild', upload_to='images/', blank=True)
    shop_url = models.URLField('Link', blank=True, help_text='Link zu einem Shop o.ä.')
    price = models.DecimalField('Preis', max_digits=6, decimal_places=2, blank=True)
    gifter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gifter', on_delete=models.SET_NULL, null=True, blank=True)
    visibility_to_owner = models.BooleanField(default='True')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wish-detail', args=[str(self.id)])