# Generated by Django 2.2.13 on 2022-02-03 08:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20220203_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_likes',
            name='liked_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 14, 14, 25, 767956)),
        ),
        migrations.AlterField(
            model_name='post_likes',
            name='liked_by',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]