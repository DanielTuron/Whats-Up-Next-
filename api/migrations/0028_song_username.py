# Generated by Django 4.1 on 2023-01-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_queue_username_alter_queue_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='username',
            field=models.CharField(default='aaaa', max_length=20),
            preserve_default=False,
        ),
    ]
