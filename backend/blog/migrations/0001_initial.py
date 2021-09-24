# Generated by Django 3.2.5 on 2021-09-16 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=240)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('post_image', models.URLField(default='https://cdn.pixabay.com/photo/2018/04/06/13/46/poly-3295856_960_720.png', max_length=500)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('truncated_body', tinymce.models.HTMLField(default='Article Intro')),
                ('body', tinymce.models.HTMLField()),
                ('meta_description', models.CharField(blank=True, max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=False)),
                ('reading_time', models.CharField(blank=True, max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.profile')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]