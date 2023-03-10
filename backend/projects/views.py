from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer