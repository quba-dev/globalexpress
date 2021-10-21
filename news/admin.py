from django.utils.html import format_html
from django.contrib import admin
from news.models import (Post, Category,
                         Shop, CategoryShop,
                         WareHouse)

@admin.register(Post)
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag']
    prepopulated_fields = {'slug': ('title',)}

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 150px; height:100px";/>'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(WareHouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo_tag']

    def logo_tag(self, obj):
        return format_html('<img src="{}" style="width: 50px; height:50px";/>'.format(obj.image.url))

    logo_tag.short_description = 'Logo'


# admin.site.register(Category)
# admin.site.register(CategoryShop)

@admin.register(CategoryShop)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}