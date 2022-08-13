from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article


class ArticleView(generic.ListView):
    model = Article
    template_name = 'index.html'
    queryset = Article.objects.filter(status=1).order_by('-date_created')
    paginate_by = 4


class AboutView(generic.CreateView):
    model = Article
    template_name = 'about.html'
    fields = '__all__'


class ArticleDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('date_created')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article.html",
            {
                "article": article,
                "comments": comments,
                "liked": liked
            }
        )