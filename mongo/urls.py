from django.urls import path
from mongo.views import monoview

urlpatterns = [
    path('mongo',monoview.as_view())
    
]

