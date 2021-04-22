from django.db import models
from taggit.managers import TaggableManager



# Create your models here.

class Folder(models.Model):
    tag = TaggableManager()

    def __str__(self):
        return self.name
    


class Bookmark(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(max_length=200)
    description = models.TextField()
    frgn_key = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
