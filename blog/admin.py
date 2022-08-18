from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'date_created', 'status')
    search_fields = ('title', 'body')
    list_filter = ('date_created', 'status')
    summernote_fields = ('body')


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):

    search_fields = ('name', 'body')
    list_display = ('name', 'article', 'body', 'date_created', 'approved')
    list_filter = ('date_created', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


