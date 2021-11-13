from rest_framework import serializers

from .models import CustomUser, MindMap, Topic


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class MindMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindMap
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
