# Generated by Django 5.0.1 on 2024-02-11 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0014_product_is_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_sale',
            new_name='for_sale',
        ),
    ]