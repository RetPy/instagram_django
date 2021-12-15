# Generated by Django 3.2.9 on 2021-11-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_alter_tag_title'),
        ('posts', '0006_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='tags.Tag', verbose_name='tag'),
        ),
    ]