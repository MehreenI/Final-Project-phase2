# Generated by Django 5.0.1 on 2024-01-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0004_category_product_delete_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]