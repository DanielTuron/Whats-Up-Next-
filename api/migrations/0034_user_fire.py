# Generated by Django 4.1 on 2023-01-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_remove_song_fire_playback_fire_user_gave_fire'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fire',
            field=models.IntegerField(default=0),
        ),
    ]
