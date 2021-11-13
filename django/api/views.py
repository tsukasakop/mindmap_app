from django.shortcuts import render
from django.views import generic

from rest_framework import viewsets, filters

from .models import MindMap, Topic, CustomUser
from .serializer import MindMapSerializer, TopicSerializer, CustomUserSerializer
# Create your views here.


class MindMapViewSet(viewsets.ModelViewSet):
    serializer_class = MindMapSerializer
    queryset = MindMap.objects.all()

    
class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()