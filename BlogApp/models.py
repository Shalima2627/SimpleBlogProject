from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_Pic = models.ImageField(upload_to='thumbnails/')
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=25)
    slug = models.SlugField()
    thumbnail = models.ImageField()
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    categories = models.ManyToManyField('Category')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    