from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('', main_views.home_view, name='home'),
    path('new_trip', main_views.new_trip_view, name='new_trip'),
    path('trip/<int:trip_pk>', main_views.trip_view, name='trip-view'),
    path('delete_trip/<int:trip_pk>', main_views.delete_trip, name='delete-trip')
]
