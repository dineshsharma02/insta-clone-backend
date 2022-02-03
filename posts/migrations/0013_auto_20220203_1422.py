# Generated by Django 2.2.13 on 2022-02-03 08:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20220203_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_likes',
            name='post_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_id', to='posts.Posts'),
        ),
        migrations.AlterField(
            model_name='post_likes',
            name='liked_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 14, 22, 14, 489970)),
        ),
    ]
