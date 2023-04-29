from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PagesView.as_view(), name='pages'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='detail'),
]
