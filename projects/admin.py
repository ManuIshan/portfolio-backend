from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ['name', 'show_in_home', 'created_at']
    list_filter = ['show_in_home']


admin.site.register(Project, ProjectAdmin)