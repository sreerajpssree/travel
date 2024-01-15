from django.db import models

# Create your models here.
class Place(models.Model):
    # Your other fields here
    # No attribute named 'object' should be defined here

    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    dis = models.TextField()

    def __str__(self):
        return self.name