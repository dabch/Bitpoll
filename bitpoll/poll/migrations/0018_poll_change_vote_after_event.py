# Generated by Django 2.2.23 on 2021-05-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0017_poll_allow_unauthenticated_vote_changes'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='change_vote_after_event',
            field=models.BooleanField(default=True),
        ),
    ]
