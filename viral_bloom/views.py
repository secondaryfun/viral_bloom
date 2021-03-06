from rest_framework import generics
from rest_framework.response import Response
from .serializers import CovidDataByDateSerializer
from .models import CovidDataByDate
from django.views import View
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect


class StateList(generics.ListCreateAPIView):
    queryset = CovidDataByDate.objects.all()
    serializer_class = CovidDataByDateSerializer

    def list(self, request, date):
        queryset = CovidDataByDate.objects.filter(date=date)
        serializer = CovidDataByDateSerializer(queryset, many=True)
        return Response(serializer.data)

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CovidDataByDate.objects.all()
    serializer_class = CovidDataByDateSerializer


class ListOfStates(View):
    def get(self, request):
        states = CovidDataByDate.objects.all()
        return render(request, 'viral_bloom/state_list.html', {'states': states})


class DetailOfState(View):
    def get(self, request, pk):
        state = CovidDataByDate.objects.get(id=pk)
        return render(request, 'viral_bloom/detail_of_state.html', {'state': state})
