from django.db import models

class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', blank=True, null=True)
    
    def __unicode__(self):
        return "%s" % self.name
