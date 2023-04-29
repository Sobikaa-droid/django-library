from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.conf import settings

from pages.models import Page


class UserRating(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    # reverse foreign key
    user_favorite = models.ForeignKey('user_favorites.UserFavorite', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.user}: {self.page.name} - ({self.rating})"

    class Meta:
        ordering = ['-pk']
