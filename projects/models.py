from django.db import models

from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField()

    cover_image = models.ImageField(upload_to="projects/covers/")
    main_image = models.ImageField(upload_to="projects/main/")

    year = models.CharField(max_length=10)

    client = models.CharField(max_length=200)
    date = models.DateField()

    category = models.CharField(max_length=200)

    hosted_link = models.URLField(blank=True)

    final_title = models.CharField(max_length=200)
    final_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    show_in_home = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="projects/gallery/")

    def __str__(self):
        return f"{self.project.name} Image"    