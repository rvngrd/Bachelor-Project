# Generated by Django 4.2.11 on 2024-05-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_slider_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=500, verbose_name='لینک'),
        ),
    ]
