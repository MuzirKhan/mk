from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Phone = models.CharField(max_length=12)

class about1(models.Model):
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Phone = models.CharField(max_length=122)

    def __str__(self):
        return self.Email 
