# Generated by Django 5.0.1 on 2024-02-04 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
    ]
