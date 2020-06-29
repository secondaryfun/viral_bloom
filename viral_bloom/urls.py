
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('statelist/', views.ListOfStates.as_view(), name='list_of_states'),
    path('statelist/<int:date>', views.DetailOfState.as_view(),
         name='detail_of_state'),
    path('', views.ListOfStates.as_view(), name='list_of_states'),
    # API Views
    path('states/<int:date>', views.StateList.as_view(), name='state_list'),
    path('states/detail/<int:pk>', views.StateDetail.as_view(), name='state_detail'),
]
