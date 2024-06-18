from django.db import models
from ckeditor.fields import RichTextField

class Tags(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Tag"
    
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    image = models.ImageField( upload_to="blog/")
    date_added = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, related_name='blogposts')
    
    post_text = RichTextField()
    
    
    def __str__(self):
        return self.title
    
