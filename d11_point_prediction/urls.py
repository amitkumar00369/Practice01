from django.urls import path
from .views import PlayerRegister,ScoreUpdate,pointByPlayer


urlpatterns = [
    path('playerSignup',PlayerRegister.as_view()),
    path('scoreUpdate/<str:name>',ScoreUpdate.as_view()),
    path("totalPoint/<str:name>",pointByPlayer.as_view())
]
