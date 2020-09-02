# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 16:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_auto_20171102_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='userAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AlId', models.IntegerField(max_length=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sId', models.IntegerField(max_length=10)),
                ('useralbum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.userAlbum')),
            ],
        ),
    ]
