# Generated by Django 5.0.1 on 2024-02-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0017_alter_product_product_rating_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=0),
        ),
    ]
