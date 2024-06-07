from django.db import models

# Create your models here.


class PlayerScoreTable(models.Model):
    name=models.CharField(max_length=128)

    ones=models.IntegerField(blank=True,null=True)
    twos=models.IntegerField(blank=True,null=True)
    three=models.IntegerField(blank=True,null=True)
    fours=models.IntegerField(blank=True,null=True)
    sixes=models.IntegerField(blank=True,null=True)
    wickets=models.IntegerField(blank=True,null=True)
    dot=models.IntegerField(blank=True,null=True)
    overs=models.IntegerField(blank=True,null=True)
    maiden=models.IntegerField(blank=True,null=True)
    wide=models.IntegerField(blank=True,null=True)
    nb=models.IntegerField(blank=True,null=True)
    catch=models.IntegerField(blank=True,null=True)
    runout=models.IntegerField(blank=True,null=True)
    total_point=models.IntegerField(null=True,blank=True)
    designations=models.CharField(max_length=50)
    style=models.CharField(max_length=256)
    int_teams=models.CharField(max_length=50)
    league_teams=models.CharField(max_length=256)
    country=models.CharField(max_length=256)
    

    
    
    
class playerList(models.Model):
    name=models.CharField(max_length=128)
    designations=models.CharField(max_length=50)
    batting_style=models.CharField(max_length=256)
    style=models.CharField(max_length=256)
    int_teams=models.CharField(max_length=50)
    league_teams=models.CharField(max_length=256)
    country=models.CharField(max_length=256)
    age=models.BigIntegerField()
    dob=models.CharField(max_length=30)
    