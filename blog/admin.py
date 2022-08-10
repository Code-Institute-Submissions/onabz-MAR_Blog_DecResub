from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'date_created', 'status')
    search_fields = ('title', 'body')
    list_filter = ('date_created', 'status')
    summernote_fields = ('body')
