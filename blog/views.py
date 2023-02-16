from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET
from django.contrib.sites.shortcuts import get_current_site

from .models import Post, Category
from .filters import PostFilter

# Create your views here.
def home(request):
    posts = Post.objects.all().prefetch_related("category")
    posts = PostFilter(request.GET, queryset=posts)
    paginator = Paginator(posts.qs, 11)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "blog/home.html",
        {"posts": page_obj, "form": posts, "main_title": "Latest Articles"},
    )


def article(request, category, slug):
    post = get_object_or_404(Post, slug=slug)
    return redirect(post.url)


def category_posts(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    if cat:
        posts = Post.objects.filter(category=cat).prefetch_related("category")
        paginator = Paginator(posts, 10)  # Show 25 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "blog/category.html",
            {"posts": page_obj, "main_title": cat.name, "form": posts},
        )


def contact(request):
    if request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        send_mail(subject, from_email=email, recipient_list=[User.objects.first().email], fail_silently=False, message=message)
    return render(request, "contact.html", {"contact": True})


def about(request):
    return render(request, "about.html")


def terms_conditions(request):
    return render(request, "terms-conditions.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")


@require_GET
def robots_txt(request):
    domain = get_current_site(request).domain
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        f"Sitemap: {domain}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
