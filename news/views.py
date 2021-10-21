from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, DetailView
from news.models import (Post, Category,
                         Shop, CategoryShop,
                         WareHouse,)


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()[:3]
        warehouse = WareHouse.objects.all
        context['posts'] = posts
        context['warehouse'] = warehouse
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'pages/detail-news.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by('-id')[:3]
        context['posts'] = posts
        return context


class NewsView(ListView):
    template_name = 'pages/news.html'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        if category == None:
            posts = Post.objects.all()[:3]
        else:
            posts = Post.objects.filter(category__slug=category)[:3]
        categories = Category.objects.all()
        context['categories'] = categories
        context['posts'] = posts
        return context


class DynamicPostsLoad(View):

    @staticmethod
    def get(request, *args, **kwargs):
        last_post_id = request.GET
        last_past_id = last_post_id.get('lastPostId')
        more_posts = Post.objects.filter(pk__gt=int(last_past_id)).values('id', 'slug','title', 'image', 'published')
        print(more_posts)
        if not more_posts:
            return JsonResponse({'data': False})
        data = []
        for post in more_posts:
            post['published'] = post['published'].strftime('%d %b %Y %H:%M')
            print(post)
            obj = {
                'id': post['id'],
                'slug': post['slug'],
                'title': post['title'],
                'image': post['image'],
                'published': post['published'],
            }
            data.append(obj)
        data[-1]['last_post'] = True
        return JsonResponse({'data': data})


class ShopView(ListView):
    template_name = 'pages/shop.html'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        if category == None:
            shops = Shop.objects.all()[:3]
        else:
            shops = Shop.objects.filter(category__slug=category)[:3]
        categories = CategoryShop.objects.all()
        context['categories'] = categories
        context['shops'] = shops
        return context


class DynamicShopsLoad(View):

    @staticmethod
    def get(request, *args, **kwargs):
        last_post_id = request.GET
        last_past_id = last_post_id.get('lastPostId')
        more_shops = Shop.objects.filter(pk__gt=int(last_past_id)).values('id', 'slug', 'title', 'image', 'logo',
                                                                          'link', 'description')
        if not more_shops:
            return JsonResponse({'data': False})
        data = []
        for shop in more_shops:
            print(shop['logo'])
            obj = {
                'id': shop['id'],
                'slug': shop['slug'],
                'title': shop['title'],
                'image': shop['image'],
                'logo': shop['logo'],
                'link': shop['link'],
                'description': shop['description'],
            }
            data.append(obj)
        data[-1]['last_post'] = True
        return JsonResponse({'data': data})