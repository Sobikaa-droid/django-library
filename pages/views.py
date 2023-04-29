from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin

from .models import Page
from user_ratings.forms import RatingForm
from user_ratings.models import UserRating
from user_favorites.models import UserFavorite


class PagesView(ListView):
    queryset = Page.objects.all()
    context_object_name = 'pages'
    paginate_by = 9
    template_name = "pages/pages.html"

    def get_queryset(self):
        order = self.request.GET.get('order_by', '-pk')
        filter_val = self.request.GET.get('filter_val', None)
        if filter_val is None:
            new_context = Page.objects.order_by(order)
        else:
            new_context = Page.objects.filter(name=filter_val)
            for i in Page.objects.all():
                if filter_val.upper() in i.name.upper():
                    new_context = Page.objects.filter(name=i.name).order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super(PagesView, self).get_context_data(**kwargs)
        return context


class PageDetailView(DetailView, ModelFormMixin):
    model = Page
    form_class = RatingForm
    template_name = "pages/page_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)

        context['rating_count'] = UserRating.objects.select_related('page').filter(page__name=self.object.name).count()
        context['pages'] = Page.objects.order_by('?')

        if self.request.user.is_authenticated:
            rate_qs = UserRating.objects.select_related('page').filter(page__name=self.object.name,
                                                                       user=self.request.user)
            fav_qs = UserFavorite.objects.select_related('page').filter(page__name=self.object.name,
                                                                        user=self.request.user)
            if rate_qs.exists():
                context['user_rating'] = rate_qs.first()

            if fav_qs.exists():
                context['favorited'] = True

        return context
