# Generated by Django 5.0.1 on 2024-02-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
