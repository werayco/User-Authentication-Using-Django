# Generated by Django 5.0.6 on 2024-08-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jangapp", "0005_alter_posts_description_alter_posts_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="description",
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name="posts",
            name="name",
            field=models.CharField(max_length=20000),
        ),
    ]
