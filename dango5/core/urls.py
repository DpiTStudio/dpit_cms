from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("articles/", views.article_list, name="article_list"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]