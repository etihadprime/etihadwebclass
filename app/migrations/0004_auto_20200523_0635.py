# Generated by Django 3.0.3 on 2020-05-23 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='ends_at',
            new_name='send_at',
        ),
    ]
