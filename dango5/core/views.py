from django.shortcuts import render, get_object_or_404
from .models import News, Portfolio, Page
from django.core.paginator import Paginator

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