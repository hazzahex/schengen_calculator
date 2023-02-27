from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_views.home_view, name='home'),
    path('new_trip', main_views.new_trip_view, name='new_trip'),
    path('trip/<int:trip_pk>', main_views.trip_view, name='trip-view'),
    path('delete_trip/<int:trip_pk>', main_views.delete_trip, name='delete-trip'),
    path('register/', main_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
]
