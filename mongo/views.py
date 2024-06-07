from django.shortcuts import render
from rest_framework.views import APIView
from mongo.models import QuestionAnswer   
from rest_framework.response import Response


class monoview(APIView):
    def post(self,request):
        
    # Example: create a new document
        qa = QuestionAnswer(
        email='example@example.com',
        name='John Doe',
        mobile_no='1234567890',
        question='What is MongoDB?',
        answer='MongoDB is a NoSQL database.'
    )
        qa.save()
        question_answers = QuestionAnswer.objects.all()

    # Prepare the data for JSON response
        data = []
        for qa in question_answers:
            data.append({
            'email': qa.email,
            'name': qa.name,
            'mobile_no': qa.mobile_no,
            'question': qa.question,
            'answer': qa.answer,
        })
    
        return Response({'message':'successfull','data':data})


# Create your views here.
