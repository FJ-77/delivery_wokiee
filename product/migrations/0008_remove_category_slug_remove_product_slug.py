# Generated by Django 4.0.3 on 2022-03-30 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_title_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
