from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
]