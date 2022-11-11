from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('add_article/', views.AddArticleView.as_view(), name='add'),
    path(
        '<slug:slug>/',
        views.ArticleDetailView.as_view(), name='article_detail'),
    path(
        'like/<slug:slug>',
        views.ArticleLike.as_view(), name='article_like'),
    path(
        'update/<slug:slug>',
        views.UpdateArticleView.as_view(), name='update_article'),
    path(
        'delete/<slug:slug>',
        views.DeleteArticleView.as_view(), name='delete_article'),
]
