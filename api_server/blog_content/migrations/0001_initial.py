# Generated by Django 4.0.2 on 2022-02-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('img_1', models.ImageField(blank=True, upload_to='covers/')),
                ('img_2', models.ImageField(blank=True, upload_to='covers/')),
            ],
        ),
    ]
