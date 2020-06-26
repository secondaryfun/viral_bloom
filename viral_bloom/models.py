from django.db import models


class State(models.Model):
    date = models.DateField()
    state = models.CharField(max_length=100)
    positive = models.IntegerField()
    death = models.IntegerField()
    recovered = models.IntegerField()

    def __str__(self):
        return self.state + " - " + self.date
