from django.urls import path

from .models import Post
from . import views

app_name = "blog"


urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("terms-conditions/", views.terms_conditions, name="terms-conditions"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
    path("<slug:slug>/", views.category_posts, name="category"),
    path("<slug:category>/<slug:slug>/", views.article, name="post"),

    path("robots.txt", views.robots_txt, name="robots_txt"),
]


