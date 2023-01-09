from django.shortcuts import render, redirect
from .utils import get_windows_trips, create_trip, get_window_start, get_trip

# Create your views here.
def home_view(request):
    trips = get_windows_trips()
    window_start = get_window_start()
    count = 0
    for trip in trips:
        if trip.start_date.date() < window_start:
            days_in_window = (trip.end_date.date() - window_start).days
            print(f'Trip at end of window')
            print(f'Days in window: {days_in_window}')
            count += days_in_window
        else:
            count += trip.day_count
    context = {
        'trips': trips,
        'count': count,
        'window_start': get_window_start()
    }
    return render(request, 'main/home.html', context=context)

def new_trip_view(request):
    context = {

    }
    if request.method == "POST":
        # print(f'POST_DATA: name:{request.POST.get("name")} start_date:{request.POST.get("start_date")} end_date:{request.POST.get("end_date")}')
        new_trip = create_trip(request.POST.get("name"), request.POST.get("start_date"), request.POST.get("end_date"))
        return redirect('home')
    else:
        return render(request, 'main/create_trip.html', context=context)

def trip_view(request, trip_pk):
    trip = get_trip(trip_pk)
    context = {
        'trip': trip
    }
    return render(request, 'main/trip.html', context=context)

def delete_trip(request, trip_pk):
    trip = get_trip(trip_pk)
    trip.delete()
    return redirect('home')