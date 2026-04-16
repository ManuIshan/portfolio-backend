from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer


def get_queryset(self):
    queryset = Project.objects.all().order_by("-created_at")
    show_in_home = self.request.query_params.get("show_in_home")

    if show_in_home is not None:
        show_in_home = show_in_home.lower()
        if show_in_home in ["1", "true", "yes"]:
            queryset = queryset.filter(show_in_home=True)
        elif show_in_home in ["0", "false", "no"]:
            queryset = queryset.filter(show_in_home=False)

    return queryset

def get_serializer_context(self):
    return {"request": self.request}

class ProjectDetailView(generics.RetrieveAPIView):
  serializer_class = ProjectSerializer

def get_object(self):
    slug = self.kwargs.get("slug")
    return get_object_or_404(Project, slug__iexact=slug)

def get_serializer_context(self):
    return {"request": self.request}