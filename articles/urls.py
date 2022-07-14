from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ArticleListView.as_view(), name="article-index"),
    path('<pk>/', views.ArticleDetailView.as_view(), name="article-detail")
]