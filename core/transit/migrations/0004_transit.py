# Generated by Django 4.2.5 on 2023-09-18 00:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transit", "0003_location"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transit",
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
            ],
        ),
    ]
