# Generated by Django 5.0.3 on 2024-04-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("obrazki", "0003_picture_description_picture_pub_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="picture",
            name="tags",
            field=models.CharField(blank=True, default="", max_length=512),
        ),
    ]