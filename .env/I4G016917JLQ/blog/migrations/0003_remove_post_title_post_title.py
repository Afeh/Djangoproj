# Generated by Django 4.0.5 on 2022-06-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_title_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Title',
            field=models.CharField(default='', max_length=250),
        ),
    ]