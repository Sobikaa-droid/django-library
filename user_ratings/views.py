from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from .models import UserRating
from .forms import RatingForm
from pages.models import Page
from user_favorites.models import UserFavorite


class RatingsView(ListView):
    context_object_name = 'ratings'
    paginate_by = 15
    template_name = "user_ratings/ratings.html"

    def get_queryset(self):
        return UserRating.objects.select_related('page', 'user_favorite').filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_count'] = UserRating.objects.filter(user=self.request.user).count()

        return context


@login_required(login_url='users:register')
def rate_page(request, slug):
    """
    1. Sets user_favorite in UserRating table if this table exists, OR creates UserRating table.
    2. Sets user_rating in UserFavorite table if this table exists,
    """
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            page_obj = get_object_or_404(Page, slug=slug)
            rating = int(request.POST.get('rating'))
            fav_qs = UserFavorite.objects.select_related('page').filter(page__slug=page_obj.slug, user=request.user)

            # 1.
            rate_obj, created = UserRating.objects.get_or_create(
                page=page_obj,
                user=request.user,
                defaults={'rating': rating, 'user_favorite': fav_qs.first()}
            )
            if not created:
                rate_obj.rating = rating
                rate_obj.user_favorite = fav_qs.first()
                rate_obj.save()

            # 2.
            if fav_qs.exists():
                rate_obj = UserRating.objects.select_related('page').get(page__slug=page_obj.slug, user=request.user)
                fav_obj = fav_qs.first()
                fav_obj.user_rating = rate_obj
                fav_obj.save()

            Page.objects.set_average_rating(slug=page_obj.slug)

        return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='users:register')
def delete_rating(request, slug):
    if request.method == 'POST':
        rate_obj = UserRating.objects.select_related('page').get(page__slug=slug, user=request.user)
        if rate_obj.user != request.user:
            raise ValidationError('User mismatch.')
        else:
            rate_obj.delete()

        Page.objects.set_average_rating(slug=slug)

        return redirect(request.META.get('HTTP_REFERER'))
