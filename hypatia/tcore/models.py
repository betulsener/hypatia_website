from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Input(models.Model):
    full_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    email=models.EmailField()
    title=models.CharField(max_length=100)
    message=models.TextField()

class About(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()

class Analysis(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()
    slug=models.SlugField(max_length=200, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super(Analysis,self).save(*args, **kwargs)
