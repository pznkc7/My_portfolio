from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.TextField()
    # created_at = models.DateTimeField(default=timezone.now)

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=200)
    date_earned = models.DateField()
    description = models.TextField(blank = True)
    certificate_link = models.URLField(blank=True)    
    image = models.ImageField(upload_to='certificate/',blank=True)

    def __str__(self):
        return self.title
