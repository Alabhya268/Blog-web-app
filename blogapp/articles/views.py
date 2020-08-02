from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms

from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {'article': article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            # save data in db
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
