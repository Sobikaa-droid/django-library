from django.db import models
from django.utils import timezone
from django.conf import settings

from pages.models import Page


class UserFavorite(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    # reverse foreign key
    user_rating = models.ForeignKey('user_ratings.UserRating', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user}: {self.page.name}"

    class Meta:
        ordering = ['-pk']
