from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleView(generic.ListView):
    model = Article
    template_name = 'index.html'
    queryset = Article.objects.filter(status=1).order_by('-date_created')
