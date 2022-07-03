from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    day = serializers.CharField()
    reminder = serializers.BooleanField()

    class Meta:
        model = Task
        fields = ('__all__')