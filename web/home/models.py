from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_images/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
