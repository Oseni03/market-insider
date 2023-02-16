from .models import Post, Category
from django.contrib.auth.models import User

def blog(request):
    return {
        "categories": Category.objects.filter(is_active=True),
        "me": User.objects.prefetch_related("account").first()
    }