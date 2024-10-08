# Generated by Django 5.0.7 on 2024-09-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0004_beverage"),
    ]

    operations = [
        migrations.CreateModel(
            name="sandwich",
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
                ("head", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("offers", models.CharField(max_length=25)),
                (
                    "img1",
                    models.FileField(
                        default=None, max_length=250, null=True, upload_to="Media/"
                    ),
                ),
            ],
        ),
    ]
