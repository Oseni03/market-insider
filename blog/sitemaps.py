from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return ["about", "contact", "terms-conditions", "privacy-policy"]

    def location(self, item):
        return reverse(item)
