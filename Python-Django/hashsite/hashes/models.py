from django.db import models


# Create your models here.
class HexText(models.Model):
    Text = models.CharField(max_length=100)
    Hex = models.TextField()

    def __str__(self):
        return self.Text
