# Generated by Django 4.1.5 on 2023-02-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Distitle', models.CharField(max_length=255)),
                ('DisDesc', models.TextField()),
            ],
        ),
    ]
