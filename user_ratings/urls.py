from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'user_ratings'

urlpatterns = [
    path('', login_required(views.RatingsView.as_view(), login_url='users:register'), name='ratings'),
    path('rate_page/<slug:slug>/', views.rate_page, name='rate_page'),
    path('delete_rating/<slug:slug>/', views.delete_rating, name='delete_rating'),
]
