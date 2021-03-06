# Generated by Django 4.0.3 on 2022-03-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_category_slug_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
