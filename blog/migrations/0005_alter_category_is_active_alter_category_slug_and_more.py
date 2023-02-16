# Generated by Django 4.1.1 on 2023-02-14 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_account_quote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(
                db_index=True, db_tablespace="category_indexes", default=True
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                blank=True, db_tablespace="category_indexes", max_length=250, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                db_tablespace="post_indexes",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="blog.category",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                blank=True, db_tablespace="post_indexes", max_length=250, null=True
            ),
        ),
    ]
