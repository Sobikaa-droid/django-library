from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages

from .models import UserFavorite
from pages.models import Page
from user_ratings.models import UserRating


class FavoritesView(ListView):
    context_object_name = 'favorites'
    paginate_by = 15
    template_name = "user_favorites/favorites.html"

    def get_queryset(self):
        return UserFavorite.objects.select_related('page', 'user_rating').filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_count'] = UserFavorite.objects.filter(user=self.request.user).count()

        return context


@login_required(login_url='users:register')
def like_page(request, slug):
    """
    1. Creates UserFavorite table.
    2. Sets user_favorite in UserRating table if this table exists.
    """
    if request.method == 'POST':
        page_obj = get_object_or_404(Page, slug=slug)
        rate_qs = UserRating.objects.select_related('page').filter(page__slug=slug, user=request.user)

        # 1.
        UserFavorite.objects.create(
            page=page_obj,
            user_rating=rate_qs.first(),
            user=request.user,
        )

        # 2.
        if rate_qs.exists():
            fav_obj = UserFavorite.objects.select_related('page').get(page__slug=slug, user=request.user)
            rate_obj = rate_qs.first()
            rate_obj.user_favorite = fav_obj
            rate_obj.save()

        messages.success(request, f'{page_obj.name} added to favorites.')
        return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='users:register')
def unlike_page(request, slug):
    if request.method == 'POST':
        fav_obj = UserFavorite.objects.select_related('page').get(page__slug=slug, user=request.user)
        if fav_obj.user != request.user:
            raise ValidationError('User mismatch.')
        else:
            fav_obj.delete()

        messages.success(request, f'{fav_obj.page.name} was removed from favorites.')
        return redirect(request.META.get('HTTP_REFERER'))
