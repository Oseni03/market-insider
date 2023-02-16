from django.urls import path
from django.contrib.sitemaps.views import sitemap, index

from .models import Post
from .sitemaps import BlogSitemap, StaticViewSitemap
from . import views

app_name = "blog"

sitemaps = {"items": BlogSitemap, "static": StaticViewSitemap}

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("terms-conditions/", views.terms_conditions, name="terms-conditions"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
    path("<slug:slug>/", views.category_posts, name="category"),
    path("<slug:category>/<slug:slug>/", views.article, name="post"),
]

sitemap_url = [
    path(
        "sitemap.xml/",
        index,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.index",
    ),
    path(
        "sitemap-<section>.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]

urlpatterns += sitemap_url
