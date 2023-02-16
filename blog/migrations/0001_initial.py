# Generated by Django 4.1 on 2023-01-02 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("rss", models.URLField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, max_length=250, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(blank=True, max_length=150, null=True)),
                ("title", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("published_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(blank=True, max_length=250, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="blog.category",
                    ),
                ),
            ],
            options={
                "ordering": ["-published_at"],
            },
        ),
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, upload_to="profile/")),
                ("quote", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "tel",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=20, null=True, region=None
                    ),
                ),
                (
                    "contact_intro",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
