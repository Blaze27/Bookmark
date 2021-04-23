from django.db import models
from taggit.managers import TaggableManager



# Create your models here.

class Folder(models.Model):
    folder_name = models.CharField(max_length=200)

    def __str__(self):
        return self.folder_name
    

class Bookmark(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(max_length=200)
    description = models.TextField()
    tag = TaggableManager()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
