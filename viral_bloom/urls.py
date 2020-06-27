
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('states/', views.StateList.as_view(), name='state_list'),
    path('statelist/', views.ListOfStates.as_view(), name='list_of_states'),
    path('statelist/<int:pk>', views.DetailOfState.as_view(), name='detail_of_state'),
    path('states/<int:pk>', views.StateDetail.as_view(), name='state_detail'),
    path('', views.ListOfStates.as_view(), name='list_of_states'),
]
