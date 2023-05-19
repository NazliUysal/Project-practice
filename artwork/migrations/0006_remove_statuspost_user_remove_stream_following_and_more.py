# Generated by Django 4.2 on 2023-05-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0005_post_art_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statuspost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='following',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='post',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='art_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='post_images'),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='StatusPost',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]