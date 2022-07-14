from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ArticleListView(ListView):

    model = Article
    context_object_name = "article_list"
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "article_detail.html"


