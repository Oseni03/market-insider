from django.contrib import admin
from .models import Post, Category, Account

# Register your models here.
admin.site.register(Category)
admin.site.register(Account)

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_filter = ['published_at']
    list_display = ('__str__', 'author', 'title')
    list_select_related = ('category',)
    list_per_page = 50