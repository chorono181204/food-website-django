# Generated by Django 5.1.2 on 2024-10-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_combo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='carbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='fats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='protein',
            field=models.IntegerField(default=0),
        ),
    ]
