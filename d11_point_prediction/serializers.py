from rest_framework import serializers
from .models import playerList,PlayerScoreTable

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=playerList
        
        fields=['id','name','age','dob','designations','style','int_teams','league_teams']
        
        
class IndividualPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlayerScoreTable
        fields=[]