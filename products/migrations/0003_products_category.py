# Generated by Django 5.0.1 on 2024-02-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_createdate_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default='women/men', max_length=100),
        ),
    ]
