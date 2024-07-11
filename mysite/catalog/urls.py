from django.contrib import admin
from django.urls import path, include
from . import views
from .views import TechnicalSpecificationListView, TechnicalSpecificationDetailView, register


urlpatterns = [
    path("", views.index, name='index'),
    path("manufacturers/", views.manufacturers, name='manufacturers'),
    path("manufacturers/<int:manufacturer_id>/", views.manufacturer, name='manufacturer'),
    path("airconditioners/", views.AirConditionerListView.as_view(), name='airconditioners'),
    path("airconditioners/<int:pk>/", views.AirConditionerDetailView.as_view(), name='airconditioner'),
    path('technicalspecifications/', TechnicalSpecificationListView.as_view(), name='technicalspecifications'),
    path('technicalspecifications/<int:pk>/', TechnicalSpecificationDetailView.as_view(), name='technicalspecification'),
    path('search/', views.search, name='search'),
    path('register/', register, name='register'),
    path('profile/', views.profile, name='profile'),
]
