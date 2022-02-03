# Generated by Django 2.2.13 on 2022-02-03 09:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20220203_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_likes',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='post_likes',
            name='liked_at',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='post_likes',
        ),
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 3, 9, 36, 40, 579842, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='total_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
    ]
