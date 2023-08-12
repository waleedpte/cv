from django.db import models

class contact_user(models.Model):
    Name = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Message = models.TextField()
    
    def __str__(self):
        return self.Name