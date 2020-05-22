# Generated by Django 3.0.4 on 2020-04-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('link', models.CharField(default='Not Found', max_length=1000, null=True)),
                ('result', models.CharField(default='Not Found', max_length=100, null=True)),
                ('flair', models.CharField(default='Not Found', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedBack',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('reply', models.TextField()),
                ('replied', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
