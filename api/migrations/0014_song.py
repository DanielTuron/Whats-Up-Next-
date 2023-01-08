# Generated by Django 4.1 on 2023-01-04 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_user_party_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('artist', models.TextField()),
                ('duration', models.IntegerField()),
                ('image_url', models.CharField(max_length=200)),
                ('time', models.IntegerField(default=0)),
                ('is_playing', models.BooleanField(default=False)),
            ],
        ),
    ]
