# Generated by Django 5.0.1 on 2024-02-03 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='createdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=500),
        ),
    ]
