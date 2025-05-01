from django.shortcuts import render
from django.views.generic import DetailView
from .models import Page, HomePage


class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page_detail.html"
    context_object_name = "page"


class HomePageDetailView(DetailView):
    model = HomePage
    template_name = "pages/home_page_detail.html"
    context_object_name = "home_page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.posts.all()
        return context
