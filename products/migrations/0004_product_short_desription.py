# Generated by Django 3.0.7 on 2020-06-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200610_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_desription',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
