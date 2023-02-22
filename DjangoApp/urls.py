from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views

from blog.sitemaps import BlogSitemap, StaticViewSitemap, CategorySitemap


sitemaps = {
    "blogs": BlogSitemap, 
    "static": StaticViewSitemap,
    "categories": CategorySitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('newsletter/', include('newsletter.urls', namespace="newsletter")),
    path('', include('blog.urls', namespace="blog")),
]

sitemap_url = [
    path(
        "sitemap.xml/",
        views.index,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.index",
    ),
    path(
        "sitemap-<section>.xml/",
        views.sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

urlpatterns += sitemap_url

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "DjangoApp.views.page_not_found_view"
handler500 = "DjangoApp.views.server_error_view"