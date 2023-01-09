from datetime import date, timedelta, datetime
from .models import Trip

def get_windows_trips():
    trips = Trip.objects.filter(end_date__gte=get_window_start())
    return trips

def create_trip(name, start_date, end_date):
    d1 = datetime.strptime(start_date, "%Y-%m-%d")
    d2 = datetime.strptime(end_date, "%Y-%m-%d")
    day_delta = round((d2 - d1).days) + 1
    new_trip = Trip(name=name, start_date=start_date, end_date=end_date, day_count=day_delta)
    new_trip.save()

def get_window_start():
    today = date.today()
    window_start = today - timedelta(days=180)
    return window_start

def get_trip(trip_pk):
    trip = Trip.objects.get(pk=trip_pk)
    return trip
