from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("manufacturers/", views.manufacturers, name='manufacturers'),
    path("manufacturers/<int:manufacturer_id>/", views.manufacturer, name='manufacturer'),
    path("airconditioners/", views.AirConditionerListView.as_view(), name='airconditioners'),
]

