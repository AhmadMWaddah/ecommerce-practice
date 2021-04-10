# Generated by Django 3.1.7 on 2021-04-10 07:55

import datetime
from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('shwcs_pk', models.AutoField(primary_key=True, serialize=False, verbose_name='Showcase ID')),
                ('shwcs_nme', models.CharField(max_length=100, verbose_name='Showcase Name')),
                ('shwcs_desc', models.TextField(max_length=1500, verbose_name='Showcase Description')),
                ('shwcs_dte', models.DateTimeField(default=datetime.time(7, 55, 18, 407855), verbose_name='Showcase Date')),
                ('shwcs_img', models.ImageField(blank=True, default=page.models.default_showcase_image, null=True, upload_to=page.models.showcase_image_path, verbose_name='Showcase Image')),
            ],
            options={
                'verbose_name': 'Showcase',
                'verbose_name_plural': 'Showcases',
            },
        ),
    ]