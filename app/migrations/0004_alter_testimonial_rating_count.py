# Generated by Django 5.1.1 on 2024-09-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating_count',
            field=models.IntegerField(),
        ),
    ]
