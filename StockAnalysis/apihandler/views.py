from django.shortcuts import render,HttpResponse
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer
# Create your views here.
class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer