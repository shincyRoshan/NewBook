from django.db import models

class Book_List(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year=models.IntegerField()
    img = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name

# Create your models here.
