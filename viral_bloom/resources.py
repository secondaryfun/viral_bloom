from .models import CovidDataByDate
from import_export import resources


class CovidDataByDateResource(resources.ModelResources):
    class Meta:
        model = CovidDataByDate
        fields = ('date', 'state', 'positive', 'death', 'recovered')
