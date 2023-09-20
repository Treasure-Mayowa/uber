# Generated by Django 4.2.2 on 2023-09-19 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0008_user_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='location', to='transit.location'),
        ),
    ]