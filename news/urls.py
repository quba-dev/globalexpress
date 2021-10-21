from django.urls import path
from news.views import (NewsView, DynamicPostsLoad, IndexView,
                        NewsDetail, ShopView, DynamicShopsLoad)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<slug:slug>/', NewsDetail.as_view(), name='detail-news'),
    path('load-more-posts/', DynamicPostsLoad.as_view(), name='load-more-posts'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('load-more-shops/', DynamicShopsLoad.as_view(), name='load-more-shops'),
]