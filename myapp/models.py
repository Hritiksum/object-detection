from django.db import models

# Create your models here.
class UserFeedBack(models.Model):
    userid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reply = models.TextField()
    replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Url(models.Model):
    created_at = models.DateTimeField(primary_key=True,auto_now_add=True)
    title= models.CharField(max_length=1000,null=True,default="Not Found")
    link = models.CharField(max_length=1000,null=True,default="Not Found")
    result = models.CharField(max_length=100,null=True,default="Not Found")
    flair = models.CharField(max_length=1000,null=True,default="Not Found")
