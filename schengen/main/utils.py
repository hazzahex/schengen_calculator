from datetime import date, timedelta, datetime, timezone
from .models import Trip


def get_windows_trips():
    trips = Trip.objects.filter(
        end_date__gte=get_window_start()).order_by('-end_date')
    return trips


def create_trip(name, start_date, end_date, current):
    d1 = datetime.strptime(start_date, "%Y-%m-%d")
    d2 = datetime.strptime(end_date, "%Y-%m-%d")
    day_delta = round((d2 - d1).days) + 1
    new_trip = Trip(name=name, start_date=start_date,
                    end_date=end_date, day_count=day_delta, current=current)
    new_trip.save()


def get_window_start():
    today = date.today()
    window_start = today - timedelta(days=180)
    return window_start


def get_trip(trip_pk):
    trip = Trip.objects.get(pk=trip_pk)
    return trip


def update_open_trip(trip_pk):
    trip = Trip.objects.get(pk=trip_pk)
    if trip.current:
        trip.end_date = datetime.now(timezone.utc)
        day_delta = round((trip.end_date - trip.start_date).days) + 1
        trip.day_count = day_delta
        trip.save()


def update_trip(trip_pk, name, start_date, end_date, current):
    trip = get_trip(trip_pk)
    trip.name = name
    trip.start_date = start_date
    trip.end_date = end_date
    day_delta = round((end_date - start_date).days) + 1
    trip.day_count = day_delta
    trip.current = current
    trip.save()
