from django.shortcuts import render, get_object_or_404
from .models import News, Portfolio, Page, Article
from django.core.paginator import Paginator
from django.core.exceptions import FieldError

def home(request):
    latest_articles = Article.objects.order_by("-created_at")[:3]  # последние 3 статьи
    return render(request, "home.html", {"articles": latest_articles})

def article_list(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "articles.html", {"articles": articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "detail.html", {"article": article})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug, is_published=True)
    
    # Получаем похожие новости (по дате публикации)
    try:
        similar_news = News.objects.filter(
            is_published=True
        ).exclude(
            id=news_item.id
        ).order_by('-published_date')[:3]
    except FieldError:
        similar_news = None
    
    return render(request, 'news/detail.html', {
        'news_item': news_item,
        'similar_news': similar_news
    })

def portfolio_list(request):
    portfolio_list = Portfolio.objects.filter(is_published=True).order_by('-created_date')
    paginator = Paginator(portfolio_list, 6)  # Показывать 6 работ на странице
    page_number = request.GET.get('page')
    portfolio = paginator.get_page(page_number)
    return render(request, 'portfolio/list.html', {'portfolio': portfolio})

def news_list(request):
    news_list = News.objects.filter(is_published=True).order_by('-published_date')
    paginator = Paginator(news_list, 6)  # Показывать 6 новостей на странице
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'news/list.html', {'news': news})

def index(request):
    news = News.objects.filter(is_published=True).order_by('-published_date')[:3]
    portfolio = Portfolio.objects.filter(is_published=True).order_by('-created_date')[:6]
    return render(request, 'index.html', {'news': news, 'portfolio': portfolio})

def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'news/list.html', {'news': news})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug, is_published=True)
    return render(request, 'news/detail.html', {'news_item': news_item})

def portfolio_list(request):
    portfolio = Portfolio.objects.filter(is_published=True).order_by('-created_date')
    return render(request, 'portfolio/list.html', {'portfolio': portfolio})

def portfolio_detail(request, slug):
    portfolio_item = get_object_or_404(Portfolio, slug=slug, is_published=True)
    return render(request, 'portfolio/detail.html', {'portfolio_item': portfolio_item})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'pages/detail.html', {'page': page})