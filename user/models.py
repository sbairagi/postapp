from django.db import models

# Create your models here.
class Userdetails(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.IntegerField()


    def __str__(self):
        return "user name is " + self.fname + " email is " + self.email


class Blogpost(models.Model):
    id = models.IntegerField(primary_key=True)
    allposts = models.TextField(max_length=5000)
    auther = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "auther name is " + self.auther