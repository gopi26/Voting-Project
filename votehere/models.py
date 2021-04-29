from django.db import models

# Create your models here.

class Canditate(models.Model):
    Name = models.CharField(max_length=30)
    Vote = models.IntegerField()

    def __str__(self):
        return str(self.id)

class votedUser(models.Model):
    voted = models.IntegerField()

    def __str__(self):
        return str(self.voted)
