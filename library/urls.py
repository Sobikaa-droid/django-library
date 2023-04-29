from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),

    path('pages/', include(('pages.urls', 'pages'))),
    path('users/', include(('users.urls', 'users'))),
    path('user_ratings/', include(('user_ratings.urls', 'user_ratings'))),
    path('user_favorites/', include(('user_favorites.urls', 'user_favorites'))),
]
