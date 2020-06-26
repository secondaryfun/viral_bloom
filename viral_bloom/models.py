from django.db import models
import csv


class CovidDataByDate(models.Model):
    date = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    positive = models.CharField(max_length=100)
    death = models.CharField(max_length=100)
    recovered = models.CharField(max_length=100)

    def __str__(self):
        return self.state + " - " + self.date

# with open('./daily.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         CovidDataByDate(date=row['date'], state=row['state'], positive=row['positive'], death=row['death'], recovered=row['recovered']).save()
