# Generated by Django 4.2.14 on 2024-08-14 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_remove_recipe_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
