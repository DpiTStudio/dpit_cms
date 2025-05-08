from django.contrib import admin
from .models import News, Portfolio, Page
from django.utils.safestring import mark_safe
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published', 'get_image')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100">')
    
    get_image.short_description = 'Изображение'

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_published', 'get_image')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100">')
    
    get_image.short_description = 'Изображение'

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Page, PageAdmin)