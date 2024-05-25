from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from article_module.models import Article, ArticleCategory, ArticleComment
from jalali_date import datetime2jalali, date2jalali


# Create your views here.


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles': articles
#         }
#         return render(request, 'article_module/articles_page.html', context)


class ArticlesListView(ListView):
    model = Article
    ordering = '-create_date'
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.\
            filter(article_id=article.id, parent=None, accepted=True).order_by('-create_date').\
            prefetch_related('articlecomment_set')
        context['count'] = ArticleComment.objects.filter(article_id=article.id, accepted=True).count()
        return context


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)
    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'article_module/components/article_categories_component.html', context)


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        new_comment = ArticleComment(
            article_id=article_id, parent_id=parent_id,
            text=article_comment, user_id=request.user.id, accepted=False)
        if article_comment == '':
            pass
        else:
            new_comment.save()
        # context = {
        #     'comments': ArticleComment.objects.
        #     filter(article_id=article_id, parent=None, accepted=True).order_by('-create_date').
        #     prefetch_related('articlecomment_set'),
        #     'comments_count': ArticleComment.objects.filter(article_id=article_id, accepted=True).count()
        # }
        # return render(request, 'article_module/includes/article_comments_partial.html', context)
    return HttpResponse('hello')
