# Generated by Django 4.2 on 2023-04-27 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_tag_remove_image_like_count_delete_like_image_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
    ]