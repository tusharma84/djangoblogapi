from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    
    #Relation Keys
    addedBy = models.ForeignKey(User,on_delete=models.CASCADE,default = 1)

    title = models.CharField(max_length=200,blank=False,default='')
    body = models.TextField(default='')
    post_image = models.ImageField(upload_to="postImage",null=True,blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):

    #Relation Keys
    post  = models.ForeignKey(Post,on_delete=models.CASCADE,default=1)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    content = models.TextField()
    addedOn = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title + " " + self.content