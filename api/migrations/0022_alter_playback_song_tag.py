# Generated by Django 4.1 on 2023-01-04 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_song_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playback',
            name='song_tag',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
