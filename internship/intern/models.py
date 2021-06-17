from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=30, blank=True)

    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='Users/%Y/%m/%d', blank=True)
    address = models.CharField(max_length=70)

    def __str__(self):
        return self.username

class Post(models.Model):
    username = models.ForeignKey(Registration, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Posts/%Y/%m/%d' , blank=True)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username.username




