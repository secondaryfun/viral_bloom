
from django1.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('states/', views.StateList.as_view(), name='state_list'),
    path('states/<int:pk>', views.StateDetail.as_view(), name='state_detail'),
]
