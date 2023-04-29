from django.shortcuts import render
from django.views.generic import ListView

from pages.models import Page


class HomeView(ListView):
    queryset = Page.objects.order_by('?')
    context_object_name = 'pages'
    template_name = "home.html"


def about(request):
    return render(request, 'about.html')
