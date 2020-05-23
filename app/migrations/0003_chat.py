# Generated by Django 3.0.3 on 2020-05-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200522_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=100, null=True)),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(max_length=300, null=True)),
                ('ends_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
