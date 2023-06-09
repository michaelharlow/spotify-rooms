# Generated by Django 4.1.5 on 2023-04-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('token', models.CharField(max_length=255)),
                ('refresh', models.CharField(max_length=255)),
                ('expires_in', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token_type', models.CharField(max_length=50)),
            ],
        ),
    ]
