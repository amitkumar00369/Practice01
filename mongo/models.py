# from django.db import models

# Create your models here.
from mongoengine import Document, StringField, EmailField

class QuestionAnswer(Document):
    email = EmailField(required=True)
    name = StringField(max_length=100, required=True)
    mobile_no = StringField(max_length=15)
    question = StringField()
    answer = StringField()

