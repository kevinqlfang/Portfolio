from rest_framework import serializers
from .models import Project

# define a serializer for the Project model that includes all of the fields
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'