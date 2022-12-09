from .views import (
    ArticleView, AboutView, AddArticleView, ArticleDetailView,
    ArticleLike, UpdateArticleView, DeleteArticleView)
from django.urls import path


urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('add_article/', AddArticleView.as_view(), name='add'),
    path(
        '<slug:slug>/',
        ArticleDetailView.as_view(), name='article_detail'),
    path(
        'like/<slug:slug>',
        ArticleLike.as_view(), name='article_like'),
    path(
        'update/<slug:slug>',
        UpdateArticleView.as_view(), name='update_article'),
    path(
        'delete/<slug:slug>',
        DeleteArticleView.as_view(), name='delete_article'),
]
