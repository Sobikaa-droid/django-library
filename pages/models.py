from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PageManager(models.Manager):
    def set_average_rating(self, slug):
        from user_ratings.models import UserRating
        try:
            rate_qs = UserRating.objects.select_related('page').filter(page__slug=slug)
            rates_list = rate_qs.values_list('rating', flat=True)
            avg_rate = sum(rates_list) / len(rates_list)
        except ZeroDivisionError:
            avg_rate = 0

        page_obj = self.get_queryset().get(slug=slug)
        page_obj.average_rating = avg_rate
        page_obj.save()


class Page(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    image = models.ImageField(upload_to='static/pages/images/')
    average_rating = models.DecimalField(default=0, max_digits=100, decimal_places=1)
    slug = models.SlugField(unique=True, blank=True)

    objects = PageManager()

    def __str__(self):
        return f"{self.name} - ({self.average_rating})"

    class Meta:
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        """
        This will generate a unique slug for each post,
        and the unique constraint on the SlugField will ensure that there are no duplicates.
        This implementation assumes that the title field will always be unique.
        """
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:detail', args=[self.slug])
