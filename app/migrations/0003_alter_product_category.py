# Generated by Django 4.1.5 on 2023-04-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MS', 'Shirts Men'), ('MHJ', 'Hoodies/Jackets Men'), ('MJ', 'Jeans Men'), ('MT', 'Trousers Men'), ('MA', 'Active Wears Men'), ('WD', 'Dresses Women'), ('WT', 'Tops Women'), ('WJ', 'Jeans Women'), ('WS', 'Skirts Women'), ('WA', 'Active Wears Women'), ('KB', 'Boys Kids'), ('KG', 'Girls Kids'), ('T', 'Trending')], max_length=3),
        ),
    ]