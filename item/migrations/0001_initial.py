# Generated by Django 3.1.7 on 2021-04-10 07:55

from django.db import migrations, models
import django.db.models.deletion
import item.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ctgry_pk', models.AutoField(primary_key=True, serialize=False, verbose_name='Category ID')),
                ('ctgry_nme', models.CharField(max_length=100, verbose_name='Category Name')),
                ('ctgry_desc', models.TextField(max_length=1500, verbose_name='Category Description')),
                ('ctgry_img', models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='Category Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['ctgry_nme'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itm_pk', models.AutoField(primary_key=True, serialize=False, verbose_name='Item ID')),
                ('itm_sku', models.CharField(max_length=20, verbose_name='Item SKU')),
                ('itm_brcd', models.CharField(max_length=20, verbose_name='Item BarCode')),
                ('itm_nme', models.CharField(max_length=100, verbose_name='Item Name')),
                ('itm_desc', models.TextField(max_length=3000, verbose_name='Item Description')),
                ('itm_prc', models.DecimalField(decimal_places=2, default='0.00', max_digits=6, verbose_name='Item Price')),
                ('itm_img', models.ImageField(blank=True, default=item.models.default_item_image, null=True, upload_to=item.models.item_image_path, verbose_name='Item Image')),
                ('itm_ctgry', models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='item.category', verbose_name='Item Category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['itm_sku'],
            },
        ),
    ]