# Generated by Django 4.2.3 on 2023-08-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_populate_default_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="tags",
            field=models.ManyToManyField(through="core.TweetTag", to="core.tag"),
        ),
    ]
