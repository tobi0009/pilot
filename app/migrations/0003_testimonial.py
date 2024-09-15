# Generated by Django 5.1.1 on 2024-09-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(blank=True, max_length=200, null=True)),
                ('rating_count', models.TextField()),
                ('username', models.CharField(max_length=50)),
                ('user_job_title', models.CharField(max_length=50)),
                ('review', models.TextField()),
            ],
        ),
    ]
