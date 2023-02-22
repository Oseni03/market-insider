from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "hourly"
    priority = 1
    
    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_at 
    
    def location(self, obj):
        return obj.get_absolute_url()


class CategorySitemap(Sitemap):
    changefreq = "hourly"
    priority = 1
    
    def items(self):
        return Category.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at 
    
    def location(self, obj):
        return obj.get_absolute_url()


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return ["about", "contact", "terms-conditions", "privacy-policy"]

    def location(self, item):
        return reverse(f"blog:{item}")
