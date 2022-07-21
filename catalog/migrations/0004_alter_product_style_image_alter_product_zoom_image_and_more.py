# Generated by Django 4.0.2 on 2022-03-04 15:06

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_variant_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='style_image',
            field=models.ImageField(blank=True, null=True, upload_to=catalog.models.Product.generate_filename),
        ),
        migrations.AlterField(
            model_name='product',
            name='zoom_image',
            field=models.ImageField(blank=True, null=True, upload_to=catalog.models.Product.generate_filename),
        ),
        migrations.CreateModel(
            name='ProductVariantImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/variants')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
