from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *


class ArticleListView(ListView):

    model = Article
    context_object_name = "article_list"
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "article_detail.html"


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article_create_form.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['author']
            # if the author name is new, create a new Author, otherwise use the existing DB entry
            author, created = Author.objects.get_or_create(full_name=author_name)
            # Create Article Object
            article = Article(
                title=form.cleaned_data['title'],
                body_text=form.cleaned_data['body_text'],
            )
            # associate it with the author and persist to the database
            article.author = author
            article.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name, {'form': form})
