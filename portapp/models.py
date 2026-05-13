from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    subject1 = models.TextField() # named as subject1 beacause subject is a also used for send_mail function

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=200)
    date_earned = models.DateField()
    description = models.TextField(blank = True)
    certificate_link = models.URLField(blank=True)    
    image = models.ImageField(upload_to='certificate/',blank=True)

    def __str__(self):
        return self.title
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='music/')
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

