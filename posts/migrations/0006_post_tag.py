# Generated by Django 3.2.9 on 2021-11-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_remove_tag_post'),
        ('posts', '0005_rename_user_like_user_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='tags.Tag'),
        ),
    ]
