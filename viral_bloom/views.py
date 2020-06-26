from rest_framework import generics
from .serializers import CovidDataByDateSerializer
from .models import CovidDataByDate

# Create your views here.


class StateList(generics.ListCreateAPIView):
    queryset = CovidDataByDate.objects.all()
    serializer_class = CovidDataByDateSerializer


class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CovidDataByDate.objects.all()
    serializer_class = CovidDataByDateSerializer
