from django.db import models

# Create your models here.

class Scatter(models.Model):
    x = models.TextField()
    y = models.TextField()

    def __str__(self):
        return "{} | {}".format(self.x, self.y)