# Generated by Django 5.0.2 on 2024-03-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sarox", "0003_customuser_designation_customuser_profile_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile_image_table",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]
