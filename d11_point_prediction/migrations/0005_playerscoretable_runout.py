# Generated by Django 5.0.2 on 2024-04-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "d11_point_prediction",
            "0004_rename_point_of_bowled_playerscoretable_total_point_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="playerscoretable",
            name="runout",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]