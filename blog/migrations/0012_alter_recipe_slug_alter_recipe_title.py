# Generated by Django 4.2.14 on 2024-11-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_recipe_calories_carbs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]