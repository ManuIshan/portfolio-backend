from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
 image = serializers.SerializerMethodField()


class Meta:
    model = ProjectImage
    fields = ["id", "image"]

def get_image(self, obj):
    request = self.context.get("request", None)
    if obj.image:
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
    return None


class ProjectSerializer(serializers.ModelSerializer):
 gallery = ProjectImageSerializer(many=True, read_only=True)
 cover_image = serializers.SerializerMethodField()
 main_image = serializers.SerializerMethodField()


class Meta:
    model = Project
    fields = "__all__"

def get_cover_image(self, obj):
    request = self.context.get("request", None)
    if obj.cover_image:
        if request:
            return request.build_absolute_uri(obj.cover_image.url)
        return obj.cover_image.url
    return None

def get_main_image(self, obj):
    request = self.context.get("request", None)
    if obj.main_image:
        if request:
            return request.build_absolute_uri(obj.main_image.url)
        return obj.main_image.url
    return None
