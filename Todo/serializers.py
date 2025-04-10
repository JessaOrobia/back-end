from rest_framework import serializers
from .models import TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'text', 'completed', 'created_at']
