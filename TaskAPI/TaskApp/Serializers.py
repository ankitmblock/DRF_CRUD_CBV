from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Task
        fields = ('id', 'task_name', 'task_desc')