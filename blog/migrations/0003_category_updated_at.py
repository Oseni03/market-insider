# Generated by Django 4.1.7 on 2023-02-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
