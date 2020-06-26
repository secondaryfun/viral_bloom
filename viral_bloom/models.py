from django.db import models


class CovidDataByDate(models.Model):
    date = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    positive = models.CharField(max_length=100)
    death = models.CharField(max_length=100)
    recovered = models.CharField(max_length=100)

    def __str__(self):
        return self.state + " - " + self.date
