from django.urls import path
from .views import CVListView

urlpatterns = [
    path("cv/", CVListView.as_view()),
]