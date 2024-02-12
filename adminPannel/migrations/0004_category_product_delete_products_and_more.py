# Generated by Django 5.0.1 on 2024-01-30 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0003_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminPannel.category')),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='answers',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='questions',
            new_name='question',
        ),
    ]
