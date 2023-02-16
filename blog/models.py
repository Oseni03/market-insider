from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="profile/")
    tel = PhoneNumberField(max_length=20, blank=True, null=True)
    contact_intro = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_author = models.CharField(max_length=255, blank=True, null=True)


class Post(models.Model):
    # source = models.CharField(max_length=150)
    author = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        "category", 
        on_delete=models.CASCADE, 
        related_name="posts",
        db_index=True, 
        db_tablespace="post_indexes"
    )
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, db_index=True, db_tablespace="post_indexes")

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("blog:post", args=[self.category.slug, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=200)
    rss = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, db_index=True, db_tablespace="category_indexes")
    is_active = models.BooleanField(default=True, db_index=True, db_tablespace="category_indexes")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(
            "blog:category",
            args=[
                self.slug,
            ],
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
