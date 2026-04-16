from rest_framework import serializers
from .models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image"]


class ProjectSerializer(serializers.ModelSerializer):
    gallery = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__" 
        
from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
   image = serializers.SerializerMethodField()

class Meta:
    model = ProjectImage
    fields = ["id", "image"]

def get_image(self, obj):
    request = self.context.get('request')
    if obj.image:
        return request.build_absolute_uri(obj.image.url)
    return None

class ProjectSerializer(serializers.ModelSerializer):

    gallery = ProjectImageSerializer(many=True, read_only=True)
    cover_image = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()

class Meta:
    model = Project
    fields = "__all__"

def get_cover_image(self, obj):
    request = self.context.get('request')
    if obj.cover_image:
        return request.build_absolute_uri(obj.cover_image.url)
    return None

def get_main_image(self, obj):
    request = self.context.get('request')
    if obj.main_image:
        return request.build_absolute_uri(obj.main_image.url)
    return None
