from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'user_favorites'

urlpatterns = [
    path('', login_required(views.FavoritesView.as_view(), login_url='users:register'), name='favorites'),
    path('like_page/<slug:slug>/', views.like_page, name='like_page'),
    path('unlike_page/<slug:slug>/', views.unlike_page, name='unlike_page'),
]
