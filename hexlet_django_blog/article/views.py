from django.shortcuts import render
from django.views import View



class ArticleView(View):


    def get(self, request, tags=None, article_id=None):
        return render(
            request,
            'articles/index.html',
            context={'tags': tags, 'article_id': article_id}
        )