from rest_framework import generics
from .models import CV
from .serializers import CVSerializer


class CVListView(generics.ListAPIView):
    queryset = CV.objects.all().order_by("-uploaded_at")
    serializer_class = CVSerializer