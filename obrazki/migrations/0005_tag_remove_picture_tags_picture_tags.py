# Generated by Django 5.0.3 on 2024-04-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("obrazki", "0004_picture_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="picture",
            name="tags",
        ),
        migrations.AddField(
            model_name="picture",
            name="tags",
            field=models.ManyToManyField(to="obrazki.tag"),
        ),
    ]
