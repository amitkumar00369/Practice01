from django.shortcuts import render
from .models import playerList,PlayerScoreTable
from .serializers import PlayerSerializer,IndividualPlayerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class PlayerRegister(APIView):
    def post(self,request):
        try:
            serialzer=PlayerSerializer(data=request.data)
            if serialzer.is_valid():
                player=serialzer.save()
                player.country=player.int_teams
                player.save()   
                return Response({'message':'player regoistered successfully','data':serialzer.data},status=400)
            else:
                return Response({'error':serialzer.errors},status=404)
        except Exception as e:
            return Response({'error':str(e)},status=500)
class ScoreUpdate(APIView):
    def post(self,request,name=None):
        try:
            if not name:
                return Response({'error':"Not Found"},status=404)
            player=playerList.objects.filter(name=name).first()
            ones=request.data.get('ones')
            twos=request.data.get('twos')
            threes=request.data.get('threes')
            fours=request.data.get('fours')
            sixes=request.data.get('sixes')
            wickets=request.data.get('wickets')
            No_ball=request.data.get('NB')
            wide=request.data.get('wide')
            runout=request.data.get('runtout')
            maiden=request.data.get('maiden')
            catch=request.data.get('catch')
            dot=request.data.get('dot')
            over=request.data.get('overs')
            serializer=IndividualPlayerSerializer(data=request.data)
            if serializer.is_valid():
                score=serializer.save()
                score.name=player.name
                score.designations=player.designations
                score.style=player.style
                score.int_teams=player.int_teams
                score.league_teams=player.league_teams
                score.country=player.country
                if ones:
                    score.ones=ones
                    score.total_point=ones
                    score.save()
                if twos:
                    score.twos=twos
                    score.total_point=twos
                    score.save()
                if threes:
                    score.threes=threes
                    score.total_point=threes
                    score.save()
                if fours:
                    score.fours=fours
                    score.total_point=6
                    score.save()
                if sixes:
                    score.sixes=sixes
                    score.total_point=8
                    score.save() 
                if wickets:
                    score.wickets=wickets
                    score.total_point=29
                    score.save()
                if No_ball:
                    score.nb=No_ball
                    score.total_point=-1
                    score.save() 
                if wide:
                    score.wide=wide
                    score.total_point=1
                    score.save()
                if runout:
                    score.runout=runout
                    score.total_point=8
                    score.save()     
                if maiden:
                    score.maiden=maiden
                    score.total_point=2
                    score.save() 
                if catch:
                    score.catch=catch
                    score.total_point=8
                    score.save()   
                if over:
                    score.overs=over
                    score.total_point=8
                    score.save()
                return Response({'message':'updated'},status=200)
        except Exception as e:
            return Response({'message':str(e)})
          
        
            
            
    
class pointByPlayer(APIView):
    def get(self,request,name=None):
        try:
            if not name:
                return Response({'error':"Not Found"})
            players=PlayerScoreTable.objects.filter(name=name).all()
            print(len(players))
            
            if not players:
                return Response({'message':"player not found"},status=404)
            total_point=0

                
            for player in players:
                total_point += player.total_point
                    

              
                
            return Response({'message':'total points by individual player','point':total_point},status=200)
                
                
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=500)