from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article
from .forms import CommentForm


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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('date_created')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "article.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class ArticleLike(View):

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)

        if article.likes.filter(id=self.request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class AddArticleView(generic.CreateView):
    model = Article
    template_name = 'add_article.html'
    fields = ('title', 'author', 'slug', 'excerpt', 'body', 'featured_image', 'status')


class UpdateArticleView(generic.UpdateView):
    model = Article
    template_name = 'update_article.html'
    fields = ('title', 'excerpt', 'body')


class DeleteArticleView(generic.DeleteView):
    model = Article
    template_name = 'delete_article.html'