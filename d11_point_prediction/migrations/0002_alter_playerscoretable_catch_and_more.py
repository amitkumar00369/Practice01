# Generated by Django 5.0.2 on 2024-04-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("d11_point_prediction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerscoretable",
            name="catch",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="dot",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="fours",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="maiden",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="nb",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="ones",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="overs",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_bowled",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_catches",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_four",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_lbw",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_maiden",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_one",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_runout",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_six",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_three",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_two",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="point_of_wicket",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="sixes",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="three",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="twos",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="wickets",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="playerscoretable",
            name="wide",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
