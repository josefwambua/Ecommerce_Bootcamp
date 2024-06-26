# Generated by Django 5.0.6 on 2024-05-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineStore', '0003_alter_category_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
