# Generated by Django 2.2 on 2019-04-18 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190418_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='cat_image',
        ),
    ]
