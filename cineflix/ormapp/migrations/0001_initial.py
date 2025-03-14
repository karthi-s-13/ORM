# Generated by Django 5.1.7 on 2025-03-14 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=20)),
                ('budget', models.IntegerField()),
                ('ott', models.CharField(max_length=50)),
            ],
        ),
    ]
