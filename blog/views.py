from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET
from django.contrib.sites.shortcuts import get_current_site

from .models import Post, Category, ContactMessage
from .filters import PostFilter

# Create your views here.
def home(request):
    posts = Post.objects.prefetch_related("category").all()
    posts = PostFilter(request.GET, queryset=posts)
    paginator = Paginator(posts.qs, 11)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": page_obj, 
        "form": posts, 
        "main_title": "Latest Articles"
    }
    
    path = request.get_full_path()
    if "?title=" in path:
        context["path"] = path
    return render(request, "blog/home.html", context)


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
        try:
            send_mail(subject, from_email=email, recipient_list=[User.objects.first().email], fail_silently=False, message=message)
        except:
            ContactMessage.objects.create(
                name=name, email=email, 
                subject=subject, 
                message=message)
        messages.success(request, "Email sent successfully. We'll get back to you soon!")
    return render(request, "contact.html", {"contact": True, "title": "Contact"})


def about(request):
    return render(request, "about.html", {"title": "About"})


def terms_conditions(request):
    return render(request, "terms-conditions.html", {"title": "Terms and conditions"})


def privacy_policy(request):
    return render(request, "privacy-policy.html", {"title": "Privacy policy"})


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
