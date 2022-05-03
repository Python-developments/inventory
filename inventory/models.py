from django.db import models


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=300)
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
