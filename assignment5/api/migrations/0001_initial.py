# Generated by Django 5.1.7 on 2025-04-09 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('sessionid', models.AutoField(primary_key=True, serialize=False)),
                ('sessionkey', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('isadmin', models.BooleanField(default=False)),
                ('isreporter', models.BooleanField(default=False)),
                ('isanalyst', models.BooleanField(default=False)),
                ('isviewer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventid', models.AutoField(primary_key=True, serialize=False)),
                ('itemid', models.CharField(max_length=100)),
                ('eventtime', models.DateTimeField(auto_now_add=True)),
                ('eventtype', models.CharField(max_length=100)),
                ('sessionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.session')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
