# Generated by Django 5.1.1 on 2024-09-14 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_lang',
            new_name='blog_image',
        ),
    ]
